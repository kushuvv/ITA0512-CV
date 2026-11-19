import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
threshold_value = int(input("Enter threshold value (0-255): "))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, segmented = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imshow("Original", image)
cv2.imshow("Segmented Image", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
