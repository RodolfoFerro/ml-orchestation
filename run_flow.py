from prefect import Client

flow_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

client = Client()
client.create_flow_run(flow_id=flow_id)
