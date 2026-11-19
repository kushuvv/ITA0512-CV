import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
watermark = image.copy()
cv2.putText(watermark, "WATERMARK", (20, image.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
result = cv2.addWeighted(image, 0.7, watermark, 0.3, 0)
cv2.imshow("Watermarked Image", result)
cv2.imwrite("watermarked_image.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
