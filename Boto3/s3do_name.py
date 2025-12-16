import boto3
name = input("Enter the file name to delete: ")
s3 = boto3.resource('s3')
bucket = s3.Bucket('babak-boto3-bucket')
bucket.Object(name).delete()
print(f"{name} has been deleted from the bucket.")