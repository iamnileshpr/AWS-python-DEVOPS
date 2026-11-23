import streamlit as st

import pandas as pd

import plotly.express as px

from aws.ec2 import get_instances

from aws.ec2 import get_instance

from aws.cloudwatch import get_cpu_metrics

from aws.sns import send_alert

from utlis.helper import health

st.set_page_config(page_title="AWS ec2 monitor",layout="wide")

st.title("AWS ec2 health monitoring dashboard")

instances=get_instances()
df=pd.DataFrame(instances)

st.subheader("AWS ec2 instances")

st.dataframe(
    df,
    use_container_width=True
)

instance = st.selectbox(
    "Select ec2 instance",
    df["Instance ID"]
)

details=get_instance(instance)

cpu,cpu_df=get_cpu_metrics(instance)

col1,col2,col3=st.columns(3)

col1.metrics(
    "cpu usage",
    f"{cpu}%"
)

col2.metrics(
    "State",
    details["State"]["Name"]
)

col3.metrics(
    "type",
    details["InstanceType"]
)

st.divider()

left,right=st.columns(2)

with left:
    st.write("EC2 details")
    st.write("Instance ID",details["InstanceId"])
    st.write(
        "Public IP:  ",details.get("PublicIpAddress","-")
    )
    st.write(
        "Private IP :",details.get("PrivateIpAddress","-")
    )
with right:
    st.write("AWS right")
    st.write("Availability zone:",details["Placement"]["AvailabilityZone"])
    st.write("LAUNCH TIME",details["LaunchTime"])
    
st.subheader("CPU utilisation")

if not cpu_df.empty:
    fig=px.line(
        cpu_df,
        x="TIME",
        y="CPU",
        marker=True,
        title="Last 1hr CPU usage"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
else:
    st.warning("NO cloud Watch me")
status=health(cpu)

if status=="Healthy":
    st.success(status)
else:
    st.error(status)

col1,col2=st.columns(2)

with col1:
    if st.button("Refresh"):
        st.rerun()
with col2:
    if st.button("Send Alert"):
        send_Alert(instance,cpu)
        st.success("Alert sent")
    
    