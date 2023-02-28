# Serverless-webapp ![aws_logo](https://github.com/Nikhil-Singh25/Images_logos/blob/main/awslogo.png)
*URL-Shortner*

This project is a serverless web application built using AWS services such as API Gateway, Lambda functions, and DynamoDB. The web application provides a simple interface to create, read, update, and delete (CRUD) items in a DynamoDB table. The API Gateway is used to provide a RESTful interface to the Lambda functions, which handle the CRUD operations. The application is entirely serverless, meaning there are no servers to manage, and it can scale automatically to handle any amount of traffic. This project can be used as a starting point for building serverless web applications on AWS.

## Architecture

The application is built using the following AWS services:

- API Gateway
- Lambda Functions
- DynamoDB
- s3 


## Getting Started
  #### you can deploy the necessary services using AWS console or by  using the Cloudformation Template [urlshortner](/urlshortner.yaml)
   
  For deploying through console below are the steps you can follow :
  
 #### 1. Create an S3 bucket  ![S3 logo](https://github.com/Nikhil-Singh25/Images_logos/blob/3fc2bd7c05e9c841ca33f9d66020f8bb1f0dcc81/s3buck.png)
* Log in to the AWS Management Console and navigate to the S3 service -> Click on "Create bucket"
* Give your bucket a unique name and choose the region closest to your users
* Leave the default settings -> click "Create bucket"

#### 2. Create dynamo DB Table  ![DynamoDB](https://github.com/Nikhil-Singh25/Images_logos/blob/18e7fc543570f94a105fa204c1f246cf9389e8e0/dynamoDB.png)
* Navigate to the DynamoDB service in the AWS Management Console -> Click on "Create table"
* Give your table a name and set the primary key to "shortUrl" (string type) -> Click on "Create"

#### 3. Create an AWS Lambda function to handle URL shortening requests ![lambda](https://github.com/Nikhil-Singh25/Images_logos/blob/3fc2bd7c05e9c841ca33f9d66020f8bb1f0dcc81/lambda.png)
* Navigate to the Lambda service in the AWS Management Console then Click on "Create function" & Choose "Author from scratch"
* Give your function a name and choose python3.8(whatever the latest version is ) as the runtime
* In the "Function code" section paste the code in [lambda.py](/lambda.py) & click on "create Function"
* Click on the "Environment variables" tab and add the following variables:</br> 
  ```
  BUCKET_NAME = your S3 bucket name
  TABLE_NAME = your DynamoDB table name
* click on "save"

#### 4.Create an API Gateway REST API  ![apigate](https://github.com/Nikhil-Singh25/Images_logos/blob/3fc2bd7c05e9c841ca33f9d66020f8bb1f0dcc81/apigate.png)
* Navigate to the API Gateway service in the AWS Management Console -> "create API" -> "REST API" -> Choose "New API" 
* Give your api a name and click on "create API"
* Click "create Resource" -> "Create method" and Choose "GET"
* Choose "Lambda Function" as the integration type(choose your created lambda function name) -> click "save" to create the API method
* Click on the "Deploy API" dropdown menu and choose "New Stage", enter a nem for the new stage and click "Deploy"

### 5.  Deploy the API :building_construction:
* In the AWS Lambda console, select your Lambda function and click on the "Add Trigger" button.
* Choose "API Gateway" from the list of trigger and select the API you created just now.
* Once the API is deployed, you can test it by clicking on the "Invoke URL" link in the "Stages" section of the API Gateway console. </br>
 This will open a new tab in your browser, where you can enter the long URL as a query parameter (e.g. https://api.example.com/shorten?longUrl=http://www.example.com) and receive the short URL as the response.

## Author :memo:

 This Serverless webapp is created by-  [@Nikhil_Singh](https://github.com/Nikhil-Singh25)
 
 Gladly accepting community contributions too to make it better! :smile:
