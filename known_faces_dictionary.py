import numpy as np
from pathlib import Path

folder = Path("known_faces")
embeddings_folder = folder/"embeddings"

known_faces = {}

for image_path in embeddings_folder.iterdir():
    if image_path.suffix.lower() == ".npy":
        known_faces[image_path.stem] = np.load(image_path)

