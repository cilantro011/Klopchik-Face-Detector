from tkinter.font import names

import insightface
from insightface.app import FaceAnalysis
import cv2
import sys
import numpy as np

from known_faces_dictionary import known_faces

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0)

def calculate_similarity(emb1, emb2):
    dot_product = np.dot(emb1, emb2)
    norm1 = np.linalg.norm(emb1)
    norm2 = np.linalg.norm(emb2)
    similarity = dot_product/(norm1 * norm2)
    return similarity

def recognize_face(unknown_embedding, known_faces, threshold=0.6):
    best_match = ""
    best_similarity = -1

    for name, known_embedding in known_faces.items():
        similarity = calculate_similarity(unknown_embedding, known_embedding)

        if similarity > best_similarity:
            best_similarity = similarity
            best_match = name

    if best_similarity >= threshold:
        return best_match
    else:
        return "Unknown"

def recognize_names():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open Camera")
        sys.exit(1)
    while True:
        
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldnot grab a frame")
            continue

        
        test_faces = app.get(frame)
        names = []
        if test_faces:
            for face in test_faces:
                names.append(recognize_face(face.embedding, known_faces, 0.6))

        return names

def draw_rectangle():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open Camera")
        sys.exit(1)
    while True:
        
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldnot grab a frame")
            continue

        
        test_faces = app.get(frame)

        if test_faces:
            
            for face in test_faces:
                name = recognize_face(face.embedding, known_faces, 0.6)
                x1, y1, x2, y2 = map(int,face.bbox)
                color = (0, 255, 0)
                thickness = 2
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)
                cv2.putText(
                frame,
                name,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2)

        cv2.imshow("Live Video", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows