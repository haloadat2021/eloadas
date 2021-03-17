import json
import boto3
from decimal import Decimal

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url='https://dynamodb.eu-west-1.amazonaws.com')
    table = dynamodb.Table('Planets')
    items = table.scan()['Items']
    
    return {
        'statusCode': 200,
        'body': json.dumps(items, cls=DecimalEncoder)
    }

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)