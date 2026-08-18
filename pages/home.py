import streamlit as st
import streamlit.components.v1 as components

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="AgriVibe",
    page_icon="🌱",
    layout="centered"
)

# ---------------- LIGHT GREEN BACKGROUND ----------------

st.markdown("""
<style>
.stApp {
    background-color: #EAF4E6;
}
</style>
""", unsafe_allow_html=True)


st.title("AgriVibe 🌱")

st.write("வணக்கம்! உங்கள் விவசாயப் பிரச்சினைகளுக்கு AgriVibe உதவும்.")

st.subheader("AgriVibe-உடன் பேசுங்கள்")

st.write("உங்கள் பயிரின் பிரச்சினையை எங்களிடம் காட்டுங்கள்.")


# =========================
# SPEAK
# =========================

st.subheader("🎤 Speak to AgriVibe")

components.html(
    """
    <!DOCTYPE html>
    <html>

    <head>

        <style>

            body {
                font-family: Arial, sans-serif;
                text-align: center;
            }

            button {
                padding: 14px 25px;
                margin: 8px;
                border: none;
                border-radius: 10px;
                font-size: 17px;
                cursor: pointer;
            }

            #start {
                background: #4CAF50;
                color: white;
            }

            #stop {
                background: #f44336;
                color: white;
            }

            #result {
                margin-top: 20px;
                padding: 15px;
                border-radius: 10px;
                background: #f2f2f2;
                min-height: 50px;
                text-align: left;
            }

        </style>

    </head>

    <body>

        <button id="start">
            🎤 Start Speaking
        </button>

        <button id="stop" disabled>
            ⏹ Stop
        </button>

        <p id="status">
            Press Start Speaking and talk.
        </p>

        <div id="result">
            Your speech will appear here...
        </div>


        <script>

            const startButton =
                document.getElementById("start");

            const stopButton =
                document.getElementById("stop");

            const status =
                document.getElementById("status");

            const result =
                document.getElementById("result");


            // Check browser support

            const SpeechRecognition =
                window.SpeechRecognition ||
                window.webkitSpeechRecognition;


            if (!SpeechRecognition) {

                status.innerText =
                    "❌ Speech recognition is not supported by this browser.";

            }

            else {

                const recognition =
                    new SpeechRecognition();

                recognition.continuous = true;

                recognition.interimResults = true;

                // Language
                recognition.lang = "en-US";


                // =================================
                // START SPEAKING
                // =================================

                startButton.onclick =
                    function() {

                        recognition.start();

                        startButton.disabled = true;

                        stopButton.disabled = false;

                        status.innerText =
                            "🔴 Listening... Speak now.";

                    };


                // =================================
                // STOP SPEAKING
                // =================================

                stopButton.onclick =
                    function() {

                        recognition.stop();

                        startButton.disabled = false;

                        stopButton.disabled = true;

                        status.innerText =
                            "✅ Speech captured.";

                    };


                // =================================
                // SPEECH RESULT
                // =================================

                recognition.onresult =
                    function(event) {

                        let finalText = "";

                        let interimText = "";


                        for (
                            let i = event.resultIndex;
                            i < event.results.length;
                            i++
                        ) {

                            let text =
                                event.results[i][0].transcript;


                            if (
                                event.results[i].isFinal
                            ) {

                                finalText += text;

                            }

                            else {

                                interimText += text;

                            }

                        }


                        result.innerText =
                            finalText + interimText;

                    };


                recognition.onerror =
                    function(event) {

                        status.innerText =
                            "❌ Error: " + event.error;

                    };


                recognition.onend =
                    function() {

                        startButton.disabled = false;

                        stopButton.disabled = true;

                    };

            }

        </script>

    </body>

    </html>
    """,

    height=350
)


# =========================
# VIDEO
# =========================

st.subheader("📹 Record your crop")

components.html(
    """
    <!DOCTYPE html>
    <html>

    <body style="text-align:center;">

        <video
            id="video"
            autoplay
            playsinline
            style="
                width:100%;
                max-width:600px;
                border-radius:12px;
                background:black;
            ">
        </video>

        <br>

        <button
            id="start"
            style="
                padding:12px 20px;
                margin:8px;
            ">
            🎥 Start Recording
        </button>

        <button
            id="stop"
            disabled
            style="
                padding:12px 20px;
                margin:8px;
            ">
            ⏹ Stop Recording
        </button>

        <p id="status">
            Opening camera...
        </p>

        <a
            id="download"
            style="display:none;"
            download="agrivibe_crop_video.webm">

            ⬇️ Save Video

        </a>


        <script>

            let video =
                document.getElementById("video");

            let startButton =
                document.getElementById("start");

            let stopButton =
                document.getElementById("stop");

            let downloadButton =
                document.getElementById("download");

            let status =
                document.getElementById("status");


            let mediaRecorder;

            let recordedChunks = [];

            let fileExtension = "webm";


            function getSupportedMimeType() {

                const formats = [

                    "video/mp4;codecs=h264,aac",

                    "video/mp4",

                    "video/webm;codecs=vp9,opus",

                    "video/webm;codecs=vp8,opus",

                    "video/webm"

                ];


                for (let format of formats) {

                    if (
                        MediaRecorder.isTypeSupported(format)
                    ) {

                        return format;

                    }

                }

                return "";

            }


            navigator.mediaDevices.getUserMedia({

                video: true,

                audio: true

            })


            .then(function(stream) {

                video.srcObject = stream;


                let mimeType =
                    getSupportedMimeType();


                if (!mimeType) {

                    status.innerText =
                        "❌ Video recording is not supported.";

                    return;

                }


                if (mimeType.includes("mp4")) {

                    fileExtension = "mp4";

                }


                mediaRecorder =
                    new MediaRecorder(
                        stream,
                        {mimeType: mimeType}
                    );


                status.innerText =
                    "✅ Camera ready";


                mediaRecorder.ondataavailable =
                    function(event) {

                        if (event.data.size > 0) {

                            recordedChunks.push(
                                event.data
                            );

                        }

                    };


                mediaRecorder.onstop =
                    function() {

                        let blob =
                            new Blob(
                                recordedChunks,
                                {type: mimeType}
                            );


                        let videoURL =
                            URL.createObjectURL(blob);


                        downloadButton.href =
                            videoURL;


                        downloadButton.download =
                            "agrivibe_crop_video."
                            + fileExtension;


                        downloadButton.style.display =
                            "inline-block";


                        status.innerText =
                            "✅ Video recorded!";

                    };


                startButton.onclick =
                    function() {

                        recordedChunks = [];

                        mediaRecorder.start();

                        startButton.disabled = true;

                        stopButton.disabled = false;

                        status.innerText =
                            "🔴 Recording...";

                    };


                stopButton.onclick =
                    function() {

                        mediaRecorder.stop();

                        startButton.disabled = false;

                        stopButton.disabled = true;

                    };

            })


            .catch(function(error) {

                status.innerText =
                    "❌ Camera permission was denied.";

                console.log(error);

            });

        </script>

    </body>

    </html>
    """,

    height=500
)


st.write("")


st.subheader("✅ Finished recording?")

if st.button(
    "➡️ Continue to Analysis",
    use_container_width=True
):

    st.switch_page("pages/analysis.py")