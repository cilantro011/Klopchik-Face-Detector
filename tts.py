from brain import get_ai_response
import subprocess
from recording import transcription

def text_to_speech(text):
    subprocess.run(["piper",
        "--model", "en_US-lessac-medium.onnx",
        "--output_file", "test_tts.wav"
    ],
    input=text,
    text=True
    )
    subprocess.run(["aplay", "test_tts.wav"])

text_to_speech(get_ai_response("Unknown", transcription))