import os
import pandas as pd

def main() -> None:

    df = GenerateDataFrame()

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

    data = {'File Name': [], 'Emotion': []}

    for wavFilePath in wavFilePaths:

        fileName = wavFilePath[(wavFilePath.rindex("/") + 1):]
        emotion = ParseEmotion(fileName)

        data['File Name'].append(fileName)
        data['Emotion'].append(emotion)

    return pd.DataFrame(data = data)

main()