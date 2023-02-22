import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List the S3 buckets in your account
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')

