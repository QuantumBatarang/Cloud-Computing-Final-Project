from google.cloud import pubsub_v1
from viz import *

project_id = "striped-history-382921"
subscription_id = "Requests-sub"

subscriber = pubsub_v1.SubscriberClient()
publisher = pubsub_v1.PublisherClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)
topicPath = ''
type=''

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received {message}.")
    vehicle_type = message.attributes['vehicle_type']
    locid = int(message.attributes['locid'])

    if(vehicle_type == 'all'):
        img = showAll(locid, "outputs")
        topicPath = publisher.topic_path(project_id, 'All')
        type = 'all'
    elif(vehicle_type == 'car'):
        img = showCars(locid, "outputs")
        topicPath = publisher.topic_path(project_id, 'Car')
        type = 'car'
    elif(vehicle_type == 'bi'):
        img = showBicycles(locid, "outputs")
        topicPath = publisher.topic_path(project_id , 'Cyclist')
        type = 'bi'
    elif(vehicle_type == 'ped'):
        img = showPedestrian(locid, "outputs")
        topicPath = publisher.topic_path(project_id, 'Pedestrian')
        type = 'ped'
    elif(vehicle_type == 'bus'):
        img = showBusesOnly(locid, "outputs")
        topicPath = publisher.topic_path(project_id, 'Bus')
        type = 'bus'
    elif(vehicle_type == 'truck'):
        img = showTrucksOnly(locid, "outputs")
        topicPath = publisher.topic_path(project_id, 'Truck')
        type = 'truck'
    elif(vehicle_type == 'suv'):
        img = showSUV(locid, "outputs")
        topicPath = publisher.topic_path(project_id, 'SUV')
        type = 'suv'
    elif(vehicle_type == 'sed'):
        img = showSedan(locid, "outputs")
        topicPath = publisher.topic_path(project_id, 'Sedan')
        type = 'sed'

    response = publisher.publish(topicPath, data=img, type=type)
    print(response.result())
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.