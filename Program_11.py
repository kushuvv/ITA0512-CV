import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
rotated = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("180 Degree Rotation", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
