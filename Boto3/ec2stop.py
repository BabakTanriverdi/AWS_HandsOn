import boto3
ec2id = input("Enter the instance ID to stop: ") # Use Amazon EC2
ec2 = boto3.resource('ec2')
ec2.Instance(ec2id).stop() 
print(f"Instance {ec2id} has been stopped.")
