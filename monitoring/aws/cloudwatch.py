#for cloud watch

import boto3

import pandas as pd

from datetime import datetime, timedelta

from config import REGION

cloudwatch=boto3.client("cloudwatch",region_name=REGION)

def get_cpu_metrics(instance_id):
    end=datetime.utcnow()
    start=end-timedelta(hours=1)

    response=cloudwatch.get_metrics_statistics(
        Namespace="AWS/EC2",
        MetriName="CPUUtilization",
        Dimensions=
            [
                {
                    "Name":"InstacneId",
                    "Value":instance_id,
                }
            ],
        StartTime=start,
        EndTime=end,
        Period=300,
        Statistics=["Average"]
    )

    points=sorted(response["Datapoints"],key=lambda x:x ["TimeStamp"])

    if len(points)==0:
        return 0,pd.DataFrame()
    df=pd.DataFrame(points)
    df["Time"]=df["TimeStamp"]
    df["CPU"]=df("Average")

    latest=round(df.iloc[-1]["CPU"],2)

    return latest,df