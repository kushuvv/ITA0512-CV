import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
x, y, width, height = 50, 50, 200, 200
roi = image[y:y + height, x:x + width]
if roi.size == 0:
    raise ValueError("ROI is outside the image")
copied = roi.copy()
result = image.copy()
result[0:height, 0:width] = copied
cv2.imshow("Original", image)
cv2.imshow("Copied ROI", copied)
cv2.imshow("ROI Pasted at Top Left", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
