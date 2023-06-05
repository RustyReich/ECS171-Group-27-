import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    pass

data = pd.read_csv("../Dataset.csv")

uniqueEmotions = data['Emotion'].unique()
numEachEmotion = {}

for emotion in uniqueEmotions:
    numEachEmotion[emotion] = len(data.loc[data['Emotion'] == emotion])

barColors = ['red', 'orange', 'yellow', 'greenyellow', 'green', 'deepskyblue', 'blue', 'purple']
plt.rcParams["figure.figsize"] = (10, 5)
plt.xlabel("Emotions")
plt.ylabel("Frequency")
plt.bar(range(len(numEachEmotion)), list(numEachEmotion.values()), align = 'center', color = barColors)
plt.xticks(range(len(numEachEmotion)), list(numEachEmotion.keys()))
plt.savefig('../Images/Emotion_Distribution.png')