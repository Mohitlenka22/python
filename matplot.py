import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2

img = Image.open(r"img.png")
numpydata  = np.asarray(img)
print(type(numpydata))
i = Image.fromarray((numpydata))
i.save('pic.png')
cv2.imshow('img1', numpydata)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(numpydata)
print(i)

