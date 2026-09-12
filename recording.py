import subprocess

def listen_and_transcribe():
    
    subprocess.run([
        "arecord",
        "-f", "S16_LE",
        "-r", "16000",
        "-c", "1",
        "-d", "5",
        "test.wav"
    ])

    result = subprocess.run([ "/home/cil/whisper.cpp/build/bin/whisper-cli", 
                            "-m", "/home/cil/whisper.cpp/models/ggml-base.en.bin",
                            "-f", "/home/cil/Klopchik-Face-Detector/test.wav",
                             "nt" ],
                            capture_output= True,
                            text = True)

    return result.stdout.strip()

print(listen_and_transcribe())