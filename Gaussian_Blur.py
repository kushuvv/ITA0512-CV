import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow("Original", image)
cv2.imshow("Gaussian Blur", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
