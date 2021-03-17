import boto3
import uuid
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url='https://dynamodb.eu-west-1.amazonaws.com')
table = dynamodb.Table('Planets')
with open('planets.json', 'r') as file:
    data = json.load(file, parse_float=Decimal)
    for planet in data:
        planet['id'] = uuid.uuid4().hex
        table.put_item(Item=planet)