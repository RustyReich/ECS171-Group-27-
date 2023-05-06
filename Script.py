import os
import pandas as pd

DATASET_PATH = "Dataset"

WavFilePaths = []

ActorFolders = os.listdir(DATASET_PATH)

for FolderName in ActorFolders:

    ActorPath = DATASET_PATH + "/" + FolderName
    WavFileNames = os.listdir(ActorPath)

    for WavFileName in WavFileNames:

        WavFilePath = ActorPath + "/" + WavFileName
        WavFilePaths.append(WavFilePath)

Data = {'File Name': []}

for WavFilePath in WavFilePaths:

    FileName = WavFilePath[(WavFilePath.rindex("/") + 1):]
    Data['File Name'].append(FileName)

Frame = pd.DataFrame(data = Data)