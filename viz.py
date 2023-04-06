import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys, getopt
import argparse
import logging
import re

def showAll(location, output):

    scale = 1
    start = 0
    end = 0
    picture = ''

    if location == 4:
        picture = '00'
        scale = 6.5
        start = 0
        end = 6
    elif location == 1:
        picture = '07'
        scale = 10.5
        start = 7
        end = 17
    elif location == 2:
        picture = '18'
        scale = 10.5
        start = 18
        end = 29
    elif location == 3:
        picture = '30'
        scale = 10.3
        start = 30
        end = 32

        
    img = plt.imread('inD-dataset-v1.0/data/'+ picture + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):

        if i < 10:
            suff = '0' + str(i)
        else:
            suff = str(i)

        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracksMeta.csv')
        
        

        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0,numTracks): #drawing first 5 tracks
            track = trackInfo.loc[trackInfo['trackId'] == j]
            # print(track.iloc[0]['recordingId'])
            vehicle = trackMetaInfo.iloc[j]['class']
            col = 'blue'
            if(vehicle == 'truck_bus'):
                col = 'red'
            elif(vehicle == 'bicycle'):
                col = 'green'
            elif(vehicle == 'pedestrian'):
                col = 'yellow'
            ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=1.0)

    ax.imshow(img)

    filepath = output+'/all_vehicles_0'+locid+'.png' 

    fig.savefig(filepath)

def showCars(location, output):
    scale = 1
    start = 0
    end = 0
    picture = ''

    if location == 4:
        picture = '00'
        scale = 6.5
        start = 0
        end = 6
    elif location == 1:
        picture = '07'
        scale = 10.5
        start = 7
        end = 17
    elif location == 2:
        picture = '18'
        scale = 10.5
        start = 18
        end = 29
    elif location == 3:
        picture = '30'
        scale = 10.3
        start = 30
        end = 32

        
    img = plt.imread('inD-dataset-v1.0/data/'+ picture + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):

        if i < 10:
            suff = '0' + str(i)
        else:
            suff = str(i)

        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracksMeta.csv')
        
        

        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0,numTracks): 
            track = trackInfo.loc[trackInfo['trackId'] == j]
            # print(track.iloc[0]['recordingId'])
            vehicle = trackMetaInfo.iloc[j]['class']
            col = 'blue'
            if(vehicle == 'truck_bus'):
                col = 'red'
            elif(vehicle == 'bicycle'):
                col = 'green'
            elif(vehicle == 'pedestrian'):
                col = 'yellow'
            if(vehicle == 'car'):
                ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=0.5)

    ax.imshow(img)

    filepath = output+'/cars_0'+locid+'.png'

    fig.savefig(filepath)

def showBicycles(location, output):
    scale = 1
    start = 0
    end = 0
    picture = ''

    if location == 4:
        picture = '00'
        scale = 6.5
        start = 0
        end = 6
    elif location == 1:
        picture = '07'
        scale = 10.5
        start = 7
        end = 17
    elif location == 2:
        picture = '18'
        scale = 10.5
        start = 18
        end = 29
    elif location == 3:
        picture = '30'
        scale = 10.3
        start = 30
        end = 32

        
    img = plt.imread('inD-dataset-v1.0/data/'+ picture + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):

        if i < 10:
            suff = '0' + str(i)
        else:
            suff = str(i)

        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracksMeta.csv')
        
        

        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0,numTracks): 
            track = trackInfo.loc[trackInfo['trackId'] == j]
            # print(track.iloc[0]['recordingId'])
            vehicle = trackMetaInfo.iloc[j]['class']
            col = 'blue'
            if(vehicle == 'truck_bus'):
                col = 'red'
            elif(vehicle == 'bicycle'):
                col = 'magenta'
            elif(vehicle == 'pedestrian'):
                col = 'yellow'
            if(vehicle == 'bicycle'):
                ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=0.5)

    ax.imshow(img)
    filepath = output+'/bicycle_0'+locid+'.png'

    fig.savefig(filepath)


def showPedestrian(location, output):
    scale = 1
    start = 0
    end = 0
    picture = ''

    if location == 4:
        picture = '00'
        scale = 6.5
        start = 0
        end = 6
    elif location == 1:
        picture = '07'
        scale = 10.5
        start = 7
        end = 17
    elif location == 2:
        picture = '18'
        scale = 10.5
        start = 18
        end = 29
    elif location == 3:
        picture = '30'
        scale = 10.3
        start = 30
        end = 32

        
    img = plt.imread('inD-dataset-v1.0/data/'+ picture + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):

        if i < 10:
            suff = '0' + str(i)
        else:
            suff = str(i)

        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracksMeta.csv')
        
        

        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0,numTracks): 
            track = trackInfo.loc[trackInfo['trackId'] == j]
            # print(track.iloc[0]['recordingId'])
            vehicle = trackMetaInfo.iloc[j]['class']
            col = 'blue'
            if(vehicle == 'truck_bus'):
                col = 'red'
            elif(vehicle == 'bicycle'):
                col = 'green'
            elif(vehicle == 'pedestrian'):
                col = 'yellow'
            if(vehicle == 'pedestrian'):
                ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=0.5)

    ax.imshow(img)
    filepath = output+'/pedestrian_0'+locid+'.png'

    fig.savefig(filepath)

def showBusesOnly(location, output):
    scale = 1
    start = 0
    end = 0
    picture = ''

    if location == 4:
        picture = '00'
        scale = 6.5
        start = 0
        end = 6
    elif location == 1:
        picture = '07'
        scale = 10.5
        start = 7
        end = 17
    elif location == 2:
        picture = '18'
        scale = 10.5
        start = 18
        end = 29
    elif location == 3:
        picture = '30'
        scale = 10.3
        start = 30
        end = 32

        
    img = plt.imread('inD-dataset-v1.0/data/'+ picture + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):

        if i < 10:
            suff = '0' + str(i)
        else:
            suff = str(i)

        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracksMeta.csv')
         
        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0, numTracks):
            track = trackInfo.loc[(trackInfo['trackId'] == j)]
            vehicle = trackMetaInfo.iloc[j]['class']
            vehicleLength = trackMetaInfo.iloc[j]['length']
            if(vehicle == 'truck_bus' and vehicleLength >= 12 and vehicleLength <= 13):  
                col = 'red'
                ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=0.5)
                

    ax.imshow(img)
    filepath = output+'/buses_0'+locid+'.png'

    fig.savefig(filepath)

def showTrucksOnly(location, output):
    scale = 1
    start = 0
    end = 0
    picture = ''

    if location == 4:
        picture = '00'
        scale = 6.5
        start = 0
        end = 6
    elif location == 1:
        picture = '07'
        scale = 10.5
        start = 7
        end = 17
    elif location == 2:
        picture = '18'
        scale = 10.5
        start = 18
        end = 29
    elif location == 3:
        picture = '30'
        scale = 10.3
        start = 30
        end = 32

        
    img = plt.imread('inD-dataset-v1.0/data/'+ picture + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):

        if i < 10:
            suff = '0' + str(i)
        else:
            suff = str(i)

        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracksMeta.csv')
         
        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0, numTracks):
            track = trackInfo.loc[(trackInfo['trackId'] == j)]
            vehicle = trackMetaInfo.iloc[j]['class']
            vehicleLength = trackMetaInfo.iloc[j]['length']
            if(vehicle == 'truck_bus' and vehicleLength > 13):  
                col = 'purple'
                ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=0.5)
                

    ax.imshow(img)
    filepath = output+'/trucks_0'+locid+'.png'

    fig.savefig(filepath)

def showSUV(location, output):
    scale = 1
    start = 0
    end = 0
    picture = ''

    if location == 4:
        picture = '00'
        scale = 6.5
        start = 0
        end = 6
    elif location == 1:
        picture = '07'
        scale = 10.5
        start = 7
        end = 17
    elif location == 2:
        picture = '18'
        scale = 10.5
        start = 18
        end = 29
    elif location == 3:
        picture = '30'
        scale = 10.3
        start = 30
        end = 32

        
    img = plt.imread('inD-dataset-v1.0/data/'+ picture + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):

        if i < 10:
            suff = '0' + str(i)
        else:
            suff = str(i)

        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracksMeta.csv')
         
        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0, numTracks):
            track = trackInfo.loc[(trackInfo['trackId'] == j)]
            vehicle = trackMetaInfo.iloc[j]['class']
            vehicleLength = trackMetaInfo.iloc[j]['length']
            if(vehicle == 'car' and vehicleLength > 3.6):  
                col = 'blue'
                ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=0.5)
                

    ax.imshow(img)
    filepath = output+'/SUVs_0'+locid+'.png'

    fig.savefig(filepath)

def showSedan(location, output):
    scale = 1
    start = 0
    end = 0
    picture = ''

    if location == 4:
        picture = '00'
        scale = 6.5
        start = 0
        end = 6
    elif location == 1:
        picture = '07'
        scale = 10.5
        start = 7
        end = 17
    elif location == 2:
        picture = '18'
        scale = 10.5
        start = 18
        end = 29
    elif location == 3:
        picture = '30'
        scale = 10.3
        start = 30
        end = 32

        
    img = plt.imread('inD-dataset-v1.0/data/'+ picture + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):

        if i < 10:
            suff = '0' + str(i)
        else:
            suff = str(i)

        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/'+ suff + '_tracksMeta.csv')
         
        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0, numTracks):
            track = trackInfo.loc[(trackInfo['trackId'] == j)]
            vehicle = trackMetaInfo.iloc[j]['class']
            vehicleLength = trackMetaInfo.iloc[j]['length']
            if(vehicle == 'car' and vehicleLength <= 3.6):  
                col = 'blue'
                ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=0.5)
                

    ax.imshow(img)
    filepath = output+'/Sedans_0'+locid+'.png'

    fig.savefig(filepath)

def run(argv=None, save_main_session=True):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--locid',
        dest='locationId',
        default='4',
        choices=['1','2','3','4'],
        help='Location Id of the intersection (from 1- 4 only)'
    )

    parser.add_argument(
        '--vehicle',
        dest='vehicle',
        choices=['car', 'truck', 'bus', 'ped', 'bi', 'all', 'sed', 'suv'],
        required=True,
        help='type of vehicle from: car, truck, bus, pedestrian(ped), bicycle(bi), all, sedan(sed), SUV(suv)')

    parser.add_argument(
        '--output',
        dest='output',
        required=True,
        help='output folder'
    )

    known_args, pipeline_args = parser.parse_known_args(argv)

    return known_args._get_kwargs()


if __name__ == "__main__":
    
    # showAll(4)
    parameters = run()

    locid = parameters[0][1]
    output = parameters[1][1]
    vehicle = parameters[2][1]

    if(vehicle == 'all'):
        showAll(int(locid), output)
    elif(vehicle == 'car'):
        showCars(int(locid), output)
    elif(vehicle == 'bi'):
        showBicycles(int(locid), output)
    elif(vehicle == 'ped'):
        showPedestrian(int(locid), output)
    elif(vehicle == 'bus'):
        showBusesOnly(int(locid), output)
    elif(vehicle == 'truck'):
        showTrucksOnly(int(locid), output)
    elif(vehicle == 'suv'):
        showSUV(int(locid), output)
    elif(vehicle == 'sed'):
        showSedan(int(locid), output)