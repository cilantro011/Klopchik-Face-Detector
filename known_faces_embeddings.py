import insightface
from insightface.app import FaceAnalysis
import cv2
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

np.save("shishir.npy", shishir)
np.save("sajan.npy", sajan)
np.save("river.npy", river)