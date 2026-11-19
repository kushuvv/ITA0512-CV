import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
height, width = image.shape[:2]
larger = cv2.resize(image, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)
smaller = cv2.resize(image, (width // 2, height // 2), interpolation=cv2.INTER_AREA)
cv2.imshow("Original", image)
cv2.imshow("Larger", larger)
cv2.imshow("Smaller", smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()
