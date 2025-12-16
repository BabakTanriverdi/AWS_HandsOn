import boto3
put_file = input("Enter the file name to upload to S3: ")   
bucket_name = input("Enter the S3 bucket name: ")

# Use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open(put_file, 'rb')
s3.Bucket(bucket_name).put_object(Key=put_file, Body=data)
print(f"File {put_file} has been uploaded to S3 bucket '{bucket_name}'.")  