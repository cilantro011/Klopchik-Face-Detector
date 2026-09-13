from face_detect import recognize_name
from recording import listen_and_transcribe
from tts import text_to_speech
from brain import get_ai_response

name = recognize_name()
print(name)

transcription = str(listen_and_transcribe())
print(transcription)

response = get_ai_response(name, transcription)
print(response)

text_to_speech(response)





