import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
# import logging
# logging.getLogger().setLevel(logging.DEBUG)

# Set up pipeline options
options = PipelineOptions(
    runner='DataflowRunner',
    project='striped-history-382921',
    temp_location='gs://ind-dataset-bucket/tmp',
    region='northamerica-northeast2',
    streaming=True
)

def print_element(element):
    print(element)

# Define the pipeline
with beam.Pipeline(options=options) as p:
    # Read from a Pub/Sub topic
    messages = (
        p
        | beam.io.ReadFromPubSub(
            topic='projects/striped-history-382921/topics/Requests',
            with_attributes=True)
        | beam.Map(print_element)
    )    
    print(messages)

    # def get_vehicle_type(message):
    # # Extract the user's preferred vehicle type from the message.
    #     # return message.attributes.get('vehicle_type')
    #     print(message.data.decode('utf-8'))
    
    # processed_message = messages | "Process Message" >> beam.Map(get_vehicle_type)

    # processed_message | beam.Map(print)

    # Process the messages as desired
    # processed_messages = (messages 
    #                         | "Process the Message" >> beam.Map(get_vehicle_type))

    # print(processed_messages)
    # # Write to a Pub/Sub topic
    # processed_messages | beam.io.WriteToPubSub(topic='projects/striped-history-382921/topics/Vehicle')

result = p.run()
result.wait()