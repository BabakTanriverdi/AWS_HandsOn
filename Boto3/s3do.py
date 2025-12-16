import boto3
bucket_name = input("Enter the S3 bucket name: ")   
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
bucket.objects.delete()