# serverless-webapp
This project is a serverless web application built using AWS services such as API Gateway, Lambda functions, and DynamoDB. The web application provides a simple interface to create, read, update, and delete (CRUD) items in a DynamoDB table. The API Gateway is used to provide a RESTful interface to the Lambda functions, which handle the CRUD operations. The application is entirely serverless, meaning there are no servers to manage, and it can scale automatically to handle any amount of traffic. This project can be used as a starting point for building serverless web applications on AWS.

## Getting Started
  #### you can deploy the necessary services using AWS console or by  using the Cloudformation Template [urlshortner](/urshortner.yaml)
   
  For deploying through console below are the steps you can follow :
  
 1. Create an S3 bucket
* Log in to the AWS Management Console and navigate to the S3 service
* Click on "Create bucket"
* Give your bucket a unique name and choose the region closest to your users
* Leave the default settings and click "Create bucket"

2. Create dynamo DB Table
* Navigate to the DynamoDB service in the AWS Management Console
* Click on "Create table"
* Give your table a name and set the primary key to "shortUrl" (string type)
Click on "Create"

3. Create an AWS Lambda function to handle URL shortening requests
* Navigate to the Lambda service in the AWS Management Console then Click on "Create function" & Choose "Author from scratch"
* Give your function a name and choose python3.8(whatever the latest version is ) as the runtime
* In the "Function code" section paste the code in [lambda.py](/lambda.py) & click on "create Function"
* Click on the "Environment variables" tab and add the following variables:</br>
  *BUCKET_NAME = your S3 bucket name
  *TABLE_NAME = your DynamoDB table name

4.

## Architecture

The application is built using the following AWS services:

- API Gateway
- Lambda Functions
- DynamoDB
- s3 

