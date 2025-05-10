import json
import uuid
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Support both API Gateway and direct test events
        if 'body' in event:
            body = json.loads(event['body']) if isinstance(event['body'], str) else event['body']
        else:
            body = event  # direct invocation, no wrapping

        account_name = body['name']
        password = body['password']
        account_id = str(uuid.uuid4())

        table.put_item(Item={
            'account_id': account_id,
            'account_name': account_name,
            'password': password
        })

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Account created', 'account_id': account_id})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
