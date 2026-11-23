import boto3

from config import REGION

from config import SNS_TOPIC_ARN

sns=boto3.client("sns",region_name=REGION)

def send_alert(instanceid,cpu):
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        subject="AWS ec2 alert",
        message=f"""
        EC2 alert

        Instance;{instance_id}

        CPU_Usage:{cpu}%

        Time: High cpu utilisation

        """
        )