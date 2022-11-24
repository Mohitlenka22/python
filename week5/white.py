import numpy as np
import cv2

arr1 = np.zeros([500, 500, 3], dtype=np.uint8)
arr2 = np.zeros([500, 500, 3], dtype=np.uint8)
arr3 = np.zeros([500, 500, 3], dtype=np.uint8)
arr1[:, :] = [255, 255, 255]
arr2[:, :] = [128, 128, 128]
arr3[:, :] = [255, 255, 0]

cv2.imshow('img1', arr1)
cv2.imshow('img2', arr2)
cv2.imshow('img3', arr2)


cv2.waitKey(0)
cv2.destroyAllWindows()

