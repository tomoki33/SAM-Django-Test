import boto3
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region_name = os.getenv('AWS_DEFAULT_REGION', 'ap-northeast-1')

dynamodb = boto3.resource(
    'dynamodb',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

table = dynamodb.Table('PersonalTrainerBot')

item = table.put_item(
    Item={
        'id': '1',
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'age': 30
    }
)
response = table.get_item(Key={'id': '1'})
item = response.get('Item')