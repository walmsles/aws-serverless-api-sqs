import json
from aws_lambda_powertools import (
    Logger, Tracer
)
from aws_lambda_powertools.utilities.batch import sqs_batch_processor    
from aws_lambda_powertools.utilities.typing import LambdaContext

from aws_xray_lambda_segment_shim import get_sqs_triggered_recorder

logger = Logger()
tracer = Tracer()
lambda_context: LambdaContext = {}

# log record and complete
def process_it(record):
    trace_header = record.get('attributes', {}).get('AWSTraceHeader', '')
    logger.info('processing it')
    logger.info(record)
    logger.info(trace_header)
    recorder = get_sqs_triggered_recorder(
        record=record,
        lambda_request_id=lambda_context.aws_request_id,
        lambda_arn=lambda_context.invoked_function_arn
    )
    
    return True

def store_context(handler, event, context):
    lambda_context = context
    return handler(event, context)



@logger.inject_lambda_context
@tracer.capture_lambda_handler
@store_context
@sqs_batch_processor(record_handler=process_it)
def handler(event, context):
    return True

