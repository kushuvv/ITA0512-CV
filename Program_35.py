import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
text = input("Enter text to display: ")
position = (30, 50)
cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("Text on Image", image)
cv2.imwrite("text_image.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
