import boto3

# Use Amazon S3
bucket_name = input("Enter the S3 bucket name: ")
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
# Delete bucket
bucket.delete()

# Print out all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
