import boto3
import pandas as pd

def upload_to_s3(file_path, bucket_name, object_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File uploaded successfully to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

def read_from_dynamodb(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    
    response = table.scan()
    data = response['Items']
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # テスト用のコード
    upload_to_s3('data/processed/processed_interactions.csv', 'your-bucket-name', 'processed_data/interactions.csv')
    user_data = read_from_dynamodb('Users')
    print(user_data.head())
    