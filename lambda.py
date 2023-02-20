import json
import boto3
import string
import random

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = "url-shortner-ddTable"

def lambda_handler(event, context):
 try:
  long_url = event['queryStringParameters']['longUrl']
 except KeyError:
  return{
        'statusCode':400,
        'headers':{'content-Type':'text/plain'},
        'body':'Bad Request: LongUrl parameter is missing'
        }
 short_id = generate_short_id()
 short_url = f"https://{s3.meta.endpoint_url.split('.')[0]}.s3.amazonaws.com/{short_id}" # creates short URL by concatenating S3 URL, HTTPs protocol and the short ID  
    
 #Store short and long URLs in DynamoDB table
 table = dynamodb.Table(table_name)
 table.put_item(Item={'shortUrl': short_url,'long_url':long_url})
    
 #Store long URL in S3 with short ID as object key
 s3.put_object(Bucket='url-shortner-s3bucket', Key=short_id, Body=long_url)
      
 return {
        'statusCode': 200,
        'headers':{'content-Type':'text/Plain'},
        'body': short_url
 }

def generate_short_id(length=8):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range (length))