TIME_TO_RECORD = 3000;

function main()
{

    const prediction = document.getElementById("prediction");
    prediction.style.display = "none";

    const progress = document.getElementById("progress");
    progress.style.display = "none";

    const record_button = document.getElementById("record_button");
    record_button.addEventListener('mouseover', function() {
        this.style.backgroundColor = "#1db965";
    }, false);
    record_button.addEventListener('mouseout', function() {
        this.style.backgroundColor = "#282828";
    }, false);

    audioChunks = [];

    navigator.mediaDevices.getUserMedia({audio: true}).then(stream => {

        recorder = new MediaRecorder(stream);
        recorder.ondataavailable = e => {

            audioChunks.push(e.data);
            if (recorder.state == "inactive")
                sendData(audioChunks);

        };

    });

    record_button.addEventListener('click', function() {

        record_button.style.display = "none";

        audioChunks = [];
        recorder.start();

        const clickTime = (new Date()).getTime();
        const progress_bar = document.getElementById("progress_bar");
        var progressInterval = setInterval(function() {

            const elapsedMS = (new Date()).getTime() - clickTime;
            const width = (elapsedMS / TIME_TO_RECORD * 100);

            progress_bar.style.width = width + "%";
            progress_bar.innerHTML = (elapsedMS / 1000).toFixed(2) + "s";

            if (width >= 100)
                clearInterval(progressInterval);

        }, 1);
        progress.style.display = "inline-block";

        setTimeout(function() { 
            
            progress.style.display = "none";
            recorder.stop(); 
        
        }, TIME_TO_RECORD);

    });

}

function sendData(audioChunks)
{

    const mediaType = audioChunks[0].type;
    const fileExtension = mediaType.substring(mediaType.indexOf("/") + 1, mediaType.indexOf(";"));

    const audioBlob = new Blob(audioChunks, {type: mediaType});

    var data = new FormData()
    data.append('file', audioBlob, "speech.".concat(fileExtension));

    fetch("http://127.0.0.1:5000/receive", { method: 'POST', body: data }).then(
        response => response.json()
    ).then(responseJSON => { displayPrediction(responseJSON) });

}

function displayPrediction(response)
{

    prediction = response.prediction;
    document.getElementById("prediction_text").textContent = "Model Predicts: ".concat(prediction);
    document.getElementById("prediction").style.display = "inline-block";

}

main();