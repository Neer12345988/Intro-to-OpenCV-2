import cv2

img = cv2.imread("jerry.png")
cv2.imshow("Normal Jez", img)
cv2.waitKey(0)

# Resizing
resized_img = cv2.resize(img, (500, 300))
cv2.imshow("Large Jez", resized_img)
cv2.waitKey(0)

cv2.destroyAllWindows()