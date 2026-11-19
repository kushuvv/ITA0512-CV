import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))
image = np.full((height, width, 3), 255, dtype=np.uint8)
box_height = max(1, height // 10)
box_width = max(1, width // 10)
image[0:box_height, 0:box_width] = (0, 0, 0)
image[0:box_height, width - box_width:width] = (255, 0, 0)
image[height - box_height:height, 0:box_width] = (0, 255, 0)
image[height - box_height:height, width - box_width:width] = (0, 0, 255)
cv2.imshow("Colored Corner Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
