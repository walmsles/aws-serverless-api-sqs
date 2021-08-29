import json
import os
from aws_lambda_powertools import (
    Logger, Tracer 
)
from aws_lambda_powertools.utilities.data_classes import (
    APIGatewayProxyEvent, event_source
)
import boto3

sqs_client = boto3.client('sqs')
THE_QUEUE = os.getenv('THE_QUEUE', '')

logger = Logger()
tracer = Tracer()

@logger.inject_lambda_context
@tracer.capture_lambda_handler
@event_source(data_class=APIGatewayProxyEvent)
def handler(event: APIGatewayProxyEvent, context):
    logger.info('start API handler')
    try:
        if not THE_QUEUE:
            raise Exception('THE_QUEUE env var not set')
        logger.info("sending message to SQS")
        logger.info(event.body)
        sqs_client.send_message(
            QueueUrl=THE_QUEUE,
            MessageBody=event.body
        )

        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "OK"})
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }

    return response
