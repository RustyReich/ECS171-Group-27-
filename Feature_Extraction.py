import os
import pandas as pd
import librosa as lr
import matplotlib.pyplot as plt
import numpy as np

def main() -> None:

    df = GenerateDataFrame()
    df.to_csv("Dataset.csv", index = False)

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

    names = []
    emotions = []
    features = []

    for wavFilePath in wavFilePaths:

        fileName = wavFilePath[(wavFilePath.rindex("/") + 1):]
        emotion = ParseEmotion(fileName)

        audioData, samplingRate = lr.load(wavFilePath)

        zeroCrossingRate = np.mean(lr.feature.zero_crossing_rate(y = audioData).T, axis = 0)
        rootMeanSquared = np.mean(lr.feature.rms(y = audioData).T, axis = 0)
        mfcc = np.mean(lr.feature.mfcc(y = audioData, sr = samplingRate).T, axis = 0)
        chroma = np.mean(lr.feature.chroma_stft(y = audioData, sr = samplingRate).T, axis = 0)
        melSpectogram = np.mean(lr.feature.melspectrogram(y = audioData, sr = samplingRate).T, axis = 0)

        names.append(fileName)
        emotions.append(emotion)
        features.append(np.hstack((zeroCrossingRate, rootMeanSquared, mfcc, chroma, melSpectogram)))

    data = pd.DataFrame(features)
    data.insert(0, 'Emotion', emotions)
    data.insert(0, 'Name', names)

    return pd.DataFrame(data = data)

if __name__ == "__main__":
    main()