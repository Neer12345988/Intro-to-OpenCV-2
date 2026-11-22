import cv2

img = cv2.imread("tom.png")
cv2.imshow("Tom", img)
cv2.waitKey(0)

# Adding a border around screen
bordered_img = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=1)
cv2.imshow("Tom Border", bordered_img)
cv2.waitKey(0)

cv2.destroyAllWindows()