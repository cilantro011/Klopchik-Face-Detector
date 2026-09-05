import insightface
from insightface.app import FaceAnalysis
import cv2
import sys
import numpy as np

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0)

image = cv2.imread("shishir.jpg")
faces = app.get(image)

image2 = cv2.imread("sajan.jpg")
faces2 = app.get(image2)

image3 = cv2.imread("river.jpg")
faces3 = app.get(image3)

shishir = faces[0].embedding
sajan = faces2[0].embedding
river = faces3[0].embedding

known_faces = {"shishir": shishir, "sajan": sajan, "river": river}

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
        print(f"Best match: {best_match}")
    else:
        print("No match found")

test_image = cv2.imread("test_sajan.JPG")
test_faces = app.get(test_image)

test_embedding = test_faces[0].embedding

recognize_face(test_embedding, known_faces, 0.6)
