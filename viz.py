import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys, getopt

# recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/30_recordingMeta.csv')
# trackInfo = pd.read_csv('inD-dataset-v1.0/data/30_tracks.csv')
# trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/30_tracksMeta.csv')
# img = plt.imread('inD-dataset-v1.0/data/30_background.png')

# fig, ax = plt.subplots()

# ax.imshow(img)

# numTracks = recMetaInfo['numTracks'].loc[0]

#0-6    - locationId: 4 - scale by 6.5
#7-17   - locationId: 1 - scale by 10.5
#18-29   - locationId: 2 - scale by 10.5  
#30-32   - locationId: 3 - scale by 10.3


# for i in range(0,numTracks): #drawing first 5 tracks
#     track = trackInfo.loc[trackInfo['trackId'] == i]
#     # print(track.iloc[0]['recordingId'])
#     vehicle = trackMetaInfo.iloc[i]['class']
#     scale = 10.3
#     col = 'blue'
#     if(vehicle == 'truck_bus'):
#         col = 'red'
#     elif(vehicle == 'bicycle'):
#         col = 'green'
#     elif(vehicle == 'pedestrian'):
#         col = 'yellow'
#     ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=1.0)

# plt.show()

def showAll(location):

    scale = 1
    start = 0
    end = 0

    if location == 4:
        picture = 0
        scale = 6.5
        start = 0
        end = 6
        
    img = plt.imread('inD-dataset-v1.0/data/0'+ str(picture) + '_background.png')
    fig, ax = plt.subplots()
    
    for i in range(start, end+1):
        recMetaInfo = pd.read_csv('inD-dataset-v1.0/data/0'+ str(i) + '_recordingMeta.csv')
        trackInfo = pd.read_csv('inD-dataset-v1.0/data/0'+ str(i) + '_tracks.csv')
        trackMetaInfo = pd.read_csv('inD-dataset-v1.0/data/0'+ str(i) + '_tracksMeta.csv')
        
        

        numTracks = recMetaInfo['numTracks'].loc[0]

        for j in range(0,numTracks): #drawing first 5 tracks
            track = trackInfo.loc[trackInfo['trackId'] == j]
            # print(track.iloc[0]['recordingId'])
            vehicle = trackMetaInfo.iloc[j]['class']
            scale = 10.3
            col = 'blue'
            if(vehicle == 'truck_bus'):
                col = 'red'
            elif(vehicle == 'bicycle'):
                col = 'green'
            elif(vehicle == 'pedestrian'):
                col = 'yellow'
            ax.plot(scale*(track['xCenter']), -scale*(track['yCenter']), color=col, linewidth=1.0)

    ax.imshow(img)

def main(argv):

    opts, args = getopt.getopt(argv, "h")


if __name__ == "__main__":
    
    showAll(4)