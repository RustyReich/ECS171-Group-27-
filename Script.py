import os
import pandas as pd
import librosa as lr
import matplotlib.pyplot as plt
import numpy as np

def main() -> None:

    df = GenerateDataFrame()
    df.to_csv("Dataset.csv")

def ParseEmotion(fileName: str) -> str:

    match fileName[6:8]:

        case '01':
            return 'NEUTRAL'
        
        case '02':
            return 'CALM'
        
        case '03':
            return 'HAPPY'
        
        case '04':
            return 'SAD'
        
        case '05':
            return 'ANGRY'
        
        case '06':
            return 'FEARFUL'
        
        case '07':
            return 'DISGUST'
        
        case '08':
            return 'SURPRISED'

def GenerateDataFrame() -> pd.DataFrame:

    DATASET_PATH = "Dataset"

    wavFilePaths = []

    actorFolders = os.listdir(DATASET_PATH)

    for folderName in actorFolders:

        actorPath = DATASET_PATH + "/" + folderName
        wavFileNames = os.listdir(actorPath)

        for wavFileName in wavFileNames:

            wavFilePath = actorPath + "/" + wavFileName
            wavFilePaths.append(wavFilePath)

    data = {'Name': [], 'Emotion': [], 'ZCR': [], 'RMS': []}

    for wavFilePath in wavFilePaths:

        fileName = wavFilePath[(wavFilePath.rindex("/") + 1):]
        emotion = ParseEmotion(fileName)

        audioData, _ = lr.load(wavFilePath)

        zeroCrossingRate = np.mean(lr.feature.zero_crossing_rate(y = audioData))
        rootMeanSquared = np.mean(lr.feature.rms(y = audioData))

        data['Name'].append(fileName)
        data['Emotion'].append(emotion)
        data['ZCR'].append(zeroCrossingRate)
        data['RMS'].append(rootMeanSquared)

    return pd.DataFrame(data = data)

main()