import boto3

# Use Amazon S3
bucket_name = input("Enter the S3 bucket name: ")
client = boto3.client('s3')
response = client.delete_bucket(
    Bucket=bucket_name,
)

print(response)
