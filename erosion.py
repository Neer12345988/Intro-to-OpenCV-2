import cv2
import numpy as np

img = cv2.imread("tom.png")
cv2.imshow("Tom", img)
cv2.waitKey(0)

# Kernel used as an input for erosion
kernel = np.ones((5, 5), np.uint8)
img = cv2.erode(img, kernel)
cv2.imshow("Much better", img)
cv2.waitKey(0)

cv2.destroyAllWindows()