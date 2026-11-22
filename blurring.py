import cv2
import numpy as np

img = cv2.imread("tom.png")
cv2.imshow("Tom I", img)
cv2.waitKey(0)

# Gaussian blur
gaussian = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow("Tom II", gaussian)
cv2.waitKey(0)

# Median blur



cv2.destroyAllWindows()