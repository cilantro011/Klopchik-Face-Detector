from face_detect import recognize_names
from recording import listen_and_transcribe
from tts import text_to_speech
from brain import get_ai_response, get_greeting

names = recognize_names()
print(names)
people_at_door = ' and '.join(names)
conversation_history = []

greeting = get_greeting(people_at_door)
print(greeting)
text_to_speech(greeting)
conversation_history.append(f"Klopchik: {greeting}")
while True:
    transcription = listen_and_transcribe()
    print(transcription)  

    exit_phrases = ["goodbye", "good bye", "bye"]

    if any(phrase in transcription.lower() for phrase in exit_phrases):
        break
    
    response = get_ai_response(people_at_door, transcription, conversation_history)
    print(response)
    conversation_history.append(f"{people_at_door}: {transcription}")
    conversation_history.append(f"Klopchik: {response}")

    text_to_speech(response)

    




