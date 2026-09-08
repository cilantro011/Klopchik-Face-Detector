import insightface
from insightface.app import FaceAnalysis
import cv2
import numpy as np
from pathlib import Path

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0)

folder = Path("known_faces")
image_folder = folder/"images"
embeddings_folder = folder/"embeddings"
embeddings_folder.mkdir(exist_ok=True)

for image_path in image_folder.iterdir():
    if image_path.suffix.lower() ==".jpg":
        image = cv2.imread(str(image_path))
        faces = app.get(image)
        if len(faces) == 1:
            np.save(embeddings_folder/f"{image_path.stem}.npy", faces[0].embedding)
        else:
            print(f"Skipped image {image_path}. It had {len(faces)} faces.")
