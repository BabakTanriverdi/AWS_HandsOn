import boto3
name = input("Enter the file name to delete: ")
bucket_name = input("Enter the S3 bucket name: ")
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
bucket.Object(name).delete()
print(f"{name} has been deleted from the bucket - {bucket_name}.")