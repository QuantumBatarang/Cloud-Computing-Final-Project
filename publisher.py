from google.cloud import pubsub_v1
import json

# publish request to Requests topic 
publisher = pubsub_v1.PublisherClient()
topicPath = publisher.topic_path('striped-history-382921' , 'Requests')

message_data = b""

response = publisher.publish(topicPath, data=message_data, vehicle_type="car", locid="4")
print(response.result())

response = publisher.publish(topicPath, data=message_data, vehicle_type="all", locid="3")
print(response.result())

response = publisher.publish(topicPath, data=message_data, vehicle_type="bus", locid="1")
print(response.result())