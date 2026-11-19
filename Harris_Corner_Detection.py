import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
gray = cv2.cornerHarris(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 2, 3, 0.04)
image[gray > 0.01 * gray.max()] = [0, 0, 255]
cv2.imshow("Harris Corner Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
