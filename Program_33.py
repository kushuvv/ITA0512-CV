import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))
image = np.full((height, width, 3), 255, dtype=np.uint8)
x1, y1 = width // 4, height // 4
x2, y2 = 3 * width // 4, 3 * height // 4
cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
