import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1',
    endpoint_url='https://dynamodb.eu-west-1.amazonaws.com')

dynamodb.create_table(
    TableName='Planets',
    KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 1
        }
    )

