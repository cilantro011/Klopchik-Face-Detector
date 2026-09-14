# Klopchik Face Detector

Klopchik is a door greeter project that recognizes people at the door and talks to them.

It uses face recognition to identify visitors, speech-to-text to understand what they say, Gemini to generate responses, and Piper to speak back.

## What it does

- Detects and recognizes faces using InsightFace
- Matches faces using cosine similarity
- Recognizes multiple people at the door
- Greets known and unknown visitors differently
- Transcribes speech using whisper.cpp
- Generates responses using Gemini
- Speaks responses using Piper TTS
- Keeps conversation history during a visit
- Detects when the visitor leaves and resets for the next person

## Tech used

- Python
- OpenCV
- InsightFace
- whisper.cpp
- Gemini API
- Piper TTS

## How it works

```text
Camera
  ↓
Face Detection / Recognition
  ↓
Visitor Identity
  ↓
Speech to Text
  ↓
Gemini Response
  ↓
Text to Speech
```

## Current setup

Right now the project runs on a Linux laptop with a USB webcam, microphone, and speaker.

The goal is to use it as an actual door greeter that can recognize visitors and have short conversations with them.

## Notes

Face images, embeddings, API keys, generated audio files, and voice models are not included in the repository.