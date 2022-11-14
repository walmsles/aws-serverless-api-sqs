import json
from aws_lambda_powertools import (
    Logger, Tracer
)
from aws_lambda_powertools.utilities.batch import BatchProcessor, batch_processor, EventType  
from aws_lambda_powertools.utilities.data_classes.sqs_event import SQSRecord

logger = Logger()
tracer = Tracer()
processor = BatchProcessor(event_type=EventType.SQS)

# log record and complete
def process_it(record: SQSRecord):
    trace_header = record.get('attributes', {}).get('AWSTraceHeader', '')
    logger.info('processing it')
    logger.info(record)
    logger.info(trace_header)
    
    # Do Nothing ... end of demo code

    return True

@logger.inject_lambda_context
@tracer.capture_lambda_handler
@batch_processor(processor=processor, record_handler=process_it)
def handler(event, context):
    return processor.response()

