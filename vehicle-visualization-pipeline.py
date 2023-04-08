import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from viz import *
import logging
logging.getLogger().setLevel(logging.DEBUG)

options = PipelineOptions(
    runner='DataflowRunner',
    project='striped-history-382921',
    temp_location='gs://ind-dataset-bucket/tmp',
    region='northamerica-northeast2',
    streaming=True
)

def process_vehicle(message, vehicle_type, locid):
    # Process messages based on the user's preferred vehicle type.
    if(vehicle_type == 'all'):
        showAll(int(locid), "outputs")
    elif(vehicle_type == 'car'):
        showCars(int(locid), "outputs")
    elif(vehicle_type == 'bi'):
        showBicycles(int(locid), "outputs")
    elif(vehicle_type == 'ped'):
        showPedestrian(int(locid), "outputs")
    elif(vehicle_type == 'bus'):
        showBusesOnly(int(locid), "outputs")
    elif(vehicle_type == 'truck'):
        showTrucksOnly(int(locid), "outputs")
    elif(vehicle_type == 'suv'):
        showSUV(int(locid), "outputs")
    elif(vehicle_type == 'sed'):
        showSedan(int(locid), "outputs")

def get_vehicle_type(message):
    # Extract the user's preferred vehicle type from the message.
    return message.attributes['vehicle_type']

def get_location(message):
    # Extract the location 
    return message.attributes['locid']


with beam.Pipeline(options=options) as p:
    # Read messages from the input topic.
    messages = (p
                | beam.io.ReadFromPubSub(
                    # topic="projects/striped-history-382921/topics/Vehicle",
                    subscription="projects/striped-history-382921/subscriptions/Vehicle-sub",
                    with_attributes=True
                ))

    # Get the user's preferred vehicle type from the message.
    vehicle_type = (messages
                    | "Get Vehicle Type" >> beam.Map(get_vehicle_type))

    locid = (messages
                | "Get Location" >> beam.Map(get_location))

    

    print(messages)
    print(vehicle_type)
    print(locid)
    # Filter messages based on the user's preferred vehicle type and location.
    (messages
    | "Filter Messages" >> beam.Filter(lambda message: message.attributes['vehicle_type'] == vehicle_type.value and message.attributes['locid'] == locid.value)
    | "Process Messages" >> beam.Map(process_vehicle, vehicle_type=beam.pvalue.AsSingleton(vehicle_type), locid=beam.pvalue.AsSingleton(locid)))

result = p.run()
result.wait()
