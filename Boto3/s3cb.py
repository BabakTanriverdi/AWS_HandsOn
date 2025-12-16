import boto3
bucket_name = input("Enter the S3 bucket name (unique): ")  
# Use Amazon S3
s3 = boto3.resource ('s3')

# Create a new bucket
s3.create_bucket(Bucket=bucket_name)

# Print out all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
