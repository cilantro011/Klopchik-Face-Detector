from brain import get_ai_response
import subprocess


def text_to_speech(text):
    subprocess.run(["piper",
        "--model", "voices/en_US-hfc_female-medium.onnx",
        "--output_file", "test_tts.wav"
    ],
    input=text,
    text=True
    )
    subprocess.run(["aplay", "test_tts.wav"])

