import numpy as np
import cv2

arr = np.zeros([500, 500, 3], dtype=np.uint8)
# arr[:, :] = [128, 128, 128]
arr[:, :] = [100, 50, 0]

cv2.imshow('img', arr)

cv2.waitKey(0)
cv2.destroyAllWindows()

