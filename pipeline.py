from face_detect import recognize_names, person_still_at_door
from recording import listen_and_transcribe
from tts import text_to_speech
from brain import get_ai_response, get_greeting
import sys

while True:
    names = recognize_names()
    print(names)
    people_at_door = ' and '.join(names)
    conversation_history = []

    greeting = get_greeting(people_at_door)
    print(greeting)
    text_to_speech(greeting)
    conversation_history.append(f"Klopchik: {greeting}")

    empty_count = 0

    while True:
        transcription = listen_and_transcribe()
        print(transcription)  

        exit_phrases = ["goodbye", "good bye", "bye"]

        if "tomato" in transcription.lower():
            text_to_speech("Shutting down. Goodbye!")
            sys.exit()

        if any(phrase in transcription.lower() for phrase in exit_phrases):
            text_to_speech("Goodbye!")
            break

        if not transcription:
            empty_count += 1
            if empty_count >=3:
                if not person_still_at_door():
                    text_to_speech("No one is at the door. Goodbye!")
                    break
                else:
                    empty_count = 0
            response = get_ai_response(
                        people_at_door,
                        "[The visitor is silent.]",
                        conversation_history
                    )

            print(response)
            conversation_history.append(f"Klopchik: {response}")
            text_to_speech(response)
            continue
        else:
            empty_count = 0
        
        response = get_ai_response(people_at_door, transcription, conversation_history)
        print(response)
        conversation_history.append(f"{people_at_door}: {transcription}")
        conversation_history.append(f"Klopchik: {response}")

        text_to_speech(response)

    




