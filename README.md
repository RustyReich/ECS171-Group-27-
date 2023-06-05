# How to run demo
1. Create virtual python environment with `python -m venv environment`
2. Activate the virtual environment with `source environment/bin/activate`
3. Install required python packages with `pip install -r requirements.txt`
4. Cd into Webpage directory with `cd Webpage`
5. Run the server with `python server.py`
6. Open a web browser and connect to `localhost:5000`
    - Note: Some web browsers may not work correctly unless you have [ffmeg](https://ffmpeg.org/) installed on your machine. [Firefox](https://www.mozilla.org/en-US/firefox/new/) should work fine regardless.
7. Allow the web page to access your microphone
8. Click the record button and speak for 3 seconds
9. Wait for the server to return the models prediction.