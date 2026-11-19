import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("90 Degree Clockwise", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
