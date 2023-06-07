# How to run demo
Note: The demo may not work if you do not have [ffmpeg](https://ffmpeg.org/) installed on your computer. This is because the audio processing library we use, [Librosa](https://librosa.org/), requires it. There is some info on the bottom of [this page](https://librosa.org/doc/0.8.1/install.html#ffmpeg) for installing ffmpeg on various operating systems.
1. Create virtual python environment with `python -m venv environment`
2. Activate the virtual environment with `source environment/bin/activate`
3. Install required python packages with `pip install -r requirements.txt`
4. Cd into Webpage directory with `cd Webpage`
5. Run the server with `python server.py`
6. Open a web browser and connect to `localhost:5000`
    - Note: Some web browsers may not work correctly on your machine. I recommend first trying [Firefox](https://www.mozilla.org/en-US/firefox/new/), and then trying [Google Chrome](https://www.google.com/chrome/) if it does not work. This is because different browsers record audio in different formats, for example Firefox records in .ogg format while Chrome records in .webm. Depending on the audio codecs you have installed on your computer, some of these may not work. Our gradescope submission will also have a link to a YouTube video of the demo being run.
7. Allow the web page to access your microphone
8. Click the record button and speak for 3 seconds
9. Wait for the server to return the models prediction.

# Running Code For the Models and Other Scripts
- After installing the packages with `pip install -r requirements.txt`, you can go into the directory `Model Notebooks` and run the .ipynb files (`ANN.ipynb`, `KNN.ipynb`, `SVM.ipynb`) to generate the accuracy results.
- For the other scripts (`Feature_Extraction.py`, `Feature_Visualizations.py`, and `Data_Analysis.py`), you can go into the 'Scripts' directory and run them with `python <script_name>`. They generate plots that we used in our report, and will appear in the `Images` directory
