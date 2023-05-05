import os

DATASET_PATH = "Dataset"

WavFilePaths = []

ActorFolders = os.listdir(DATASET_PATH)

for FolderName in ActorFolders:

    ActorPath = DATASET_PATH + "/" + FolderName

    WavFileNames = os.listdir(ActorPath)

    for WavFileName in WavFileNames:

        WavFilePath = ActorPath + "/" + WavFileName

        WavFilePaths.append(WavFilePath)