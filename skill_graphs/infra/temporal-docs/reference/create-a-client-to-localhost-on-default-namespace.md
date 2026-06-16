# Create a client to localhost on default namespace
client = Temporalio::Client.connect('localhost:7233', 'default')
