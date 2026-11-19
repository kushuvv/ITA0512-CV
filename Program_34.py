import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))
image = np.full((height, width, 3), 255, dtype=np.uint8)
center = (width // 2, height // 2)
radius = min(width, height) // 4
cv2.circle(image, center, radius, (255, 0, 0), 3)
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
