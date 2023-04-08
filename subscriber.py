from google.cloud import pubsub_v1
import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

project_id = "striped-history-382921"

subscriber = pubsub_v1.SubscriberClient()
subscription_path_all = subscriber.subscription_path(project_id, 'All-sub')
subscription_path_bus = subscriber.subscription_path(project_id, 'Bus-sub')
subscription_path_car = subscriber.subscription_path(project_id, 'Car-sub')
subscription_path_bi = subscriber.subscription_path(project_id, 'Cyclist-sub')
subscription_path_ped = subscriber.subscription_path(project_id, 'Pedestrian-sub')
subscription_path_sed = subscriber.subscription_path(project_id, 'Sedan-sub')
subscription_path_suv = subscriber.subscription_path(project_id, 'SUV-sub')
subscription_path_truck = subscriber.subscription_path(project_id, 'Truck-sub')

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received {message}.")
    image_file = io.BytesIO(message.data)
    img = mpimg.imread(image_file, format='png')
    plt.imshow(img)
    plt.savefig('outputs/{}-image.png'.format(message.attributes["type"]))
    message.ack()

# All subscriber
streaming_pull_future_all = subscriber.subscribe(subscription_path_all, callback=callback)
print(f"Listening for messages on {subscription_path_all}..\n")

# Bus subscriber
streaming_pull_future_bus = subscriber.subscribe(subscription_path_bus, callback=callback)
print(f"Listening for messages on {subscription_path_bus}..\n")

# Car subscriber
streaming_pull_future_car = subscriber.subscribe(subscription_path_car, callback=callback)
print(f"Listening for messages on {subscription_path_car}..\n")

# Cyclist subscriber
streaming_pull_future_bi = subscriber.subscribe(subscription_path_bi, callback=callback)
print(f"Listening for messages on {subscription_path_bi}..\n")

# Pedestrian subscriber
streaming_pull_future_ped = subscriber.subscribe(subscription_path_ped, callback=callback)
print(f"Listening for messages on {subscription_path_ped}..\n")

# Sedan subscriber
streaming_pull_future_sed = subscriber.subscribe(subscription_path_sed, callback=callback)
print(f"Listening for messages on {subscription_path_sed}..\n")

# SUV subscriber
streaming_pull_future_suv = subscriber.subscribe(subscription_path_suv, callback=callback)
print(f"Listening for messages on {subscription_path_suv}..\n")

# Truck subscriber
streaming_pull_future_truck = subscriber.subscribe(subscription_path_truck, callback=callback)
print(f"Listening for messages on {subscription_path_truck}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future_all.result()
        streaming_pull_future_bus.result()
        streaming_pull_future_car.result()
        streaming_pull_future_bi.result()
        streaming_pull_future_ped.result()
        streaming_pull_future_sed.result()
        streaming_pull_future_suv.result()
        streaming_pull_future_truck.result()
    except TimeoutError:
        streaming_pull_future_all.cancel()  # Trigger the shutdown.
        streaming_pull_future_all.result()  # Block until the shutdown is complete.

        streaming_pull_future_bus.cancel()  # Trigger the shutdown.
        streaming_pull_future_bus.result()  # Block until the shutdown

        streaming_pull_future_car.cancel()  # Trigger the shutdown.
        streaming_pull_future_car.result()  # Block until the shutdown

        streaming_pull_future_bi.cancel()  # Trigger the shutdown.
        streaming_pull_future_bi.result()  # Block until the shutdown

        streaming_pull_future_ped.cancel()  # Trigger the shutdown.
        streaming_pull_future_ped.result()  # Block until the shutdown

        streaming_pull_future_sed.cancel()  # Trigger the shutdown.
        streaming_pull_future_sed.result()  # Block until the shutdown

        streaming_pull_future_suv.cancel()  # Trigger the shutdown.
        streaming_pull_future_suv.result()  # Block until the shutdown

        streaming_pull_future_truck.cancel()  # Trigger the shutdown.
        streaming_pull_future_truck.result()  # Block until the shutdown