import cv2

img = cv2.imread("tom.png")
cv2.imshow("Tom", img)
cv2.waitKey(0)

bordered_img = cv2.copyMakeBorder(img, 100, 100, 100, 130, cv2.BORDER_REFLECT, value=1)
cv2.imshow("Reflected Tom Border", bordered_img)
cv2.waitKey(0)

cv2.destroyAllWindows()