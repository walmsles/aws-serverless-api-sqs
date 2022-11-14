# AWS Serverless API gateway to SQS example

A Project allowing data posted to an API Gateway to be forwarded to an SQS queue for procesing.  This is a classic 2 step asynchronous processing pattern.

The Lambda code leverages [AWS Lambda Powertools for Python](https://github.com/awslabs/aws-lambda-powertools-python) to make applying AWS Serverless Best Practices simple and easy.

## DISCLAIMER

This is not production ready code and is provided here as an exmaple use case for AWS Lambda Powertools.  It is provided as-is and without any warranty of correctness, please use it as you wish and at your own risk :-)

## API Code - api.py

This lambda code uses APIProxyGatewayEvent models to make interacting with the event quick and easy and enables type hinting in the IDE which is really valuable.

## SQS Processing Lambda - sqs-processor.py

This lambda leverages the SQS Batch processing utility from Powertools and is an invaluable utility for SQS processing.  

# Deploying the Project to your AWS Account

Deployment is a straight forward process and assumes you have aws-cli installed, connected to your account and working.  If you need any help getting that going I have a blog articl on allowing AWS Cli access to your account with MFA enabled, catch it [here](http://www.walmsles.io/posts/securing-aws-cli/).  

This repo also assumes you have python 3.9 and [poetry](https://python-poetry.org/) installed and working.  All dependencies will be installed via npm and poetry.

To deploy this project you will need to do the following:

```ShellSession
$ npm install
$ poetry install
$ npx sls deploy
``` 