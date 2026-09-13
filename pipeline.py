from face_detect import recognize_name
from recording import listen_and_transcribe
from tts import text_to_speech
from brain import get_ai_response

name = recognize_name()
print(name)

conversation_history = []

while True:
    transcription = listen_and_transcribe()
    print(transcription)
   

    if "goodbye"in transcription.lower():
        break
    
    response = get_ai_response(name, transcription, conversation_history)
    print(response)
    conversation_history.append(f"{name}: {transcription}")
    conversation_history.append(f"AI: {response}")

    text_to_speech(response)

    




