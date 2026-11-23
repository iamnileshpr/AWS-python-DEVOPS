import boto3

from config import REGION

ec2=boto3.client("ec2",region_name=REGION)

def get_instances():
    response=ec2.describe_instances()
    instances=[]
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            name="NO NAME"
            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"]=="Name":
                        name=tag["Value"]
            instances.append({
                "Name":name,
                "Instances ID":instance["InstanceId"],
                "State":instance["InstanceType"],
                "Instance Type":instance["InstanceType"],
                "Public IP":instance.get("PublicIpAddress","-"),
                "Private IP":instance.get("PrivateIpAddress","-"),
                "Availability Zone":instance["Placement"]["AvailabilityZone"],
                "Launch Time":instance["LaunchTime"]
            })        
def get_instance(instance_id):
    response=ec2.describe_instances(
        InstanceIds=[Instance_id],
        
    )
    
