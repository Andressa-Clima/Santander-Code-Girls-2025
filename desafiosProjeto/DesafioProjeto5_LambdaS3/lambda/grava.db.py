import json
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")
table = dynamodb.Table('NotasFiscais')

def lambda_handler(event, context):
    print("Evento recebido:", event)
    
    for record in event['Records']:
        payload = record['body'] if 'body' in record else record['s3']['object']['key']
        item = {
            'id': payload.split('.')[0],
            'arquivo': payload,
            'status': 'Processado'
        }
        table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Arquivo processado com sucesso!')
    }
