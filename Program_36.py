import cv2
import numpy as np

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([int(input("Lower H: ")), int(input("Lower S: ")), int(input("Lower V: "))])
upper = np.array([int(input("Upper H: ")), int(input("Upper S: ")), int(input("Upper V: "))])
mask = cv2.inRange(hsv, lower, upper)
background = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
cv2.imshow("Background Subtraction", background)
cv2.waitKey(0)
cv2.destroyAllWindows()
