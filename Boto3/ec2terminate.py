import boto3
ec2id = input("Enter the instance ID to terminate: ")
# Use Amazon EC2
ec2 = boto3.resource('ec2')
ec2.Instance(ec2id).terminate()
print(f"Instance {ec2id} has been terminated.")