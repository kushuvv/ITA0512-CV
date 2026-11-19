import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
cascade_path = cv2.data.haarcascades + "haarcascade_eye.xml"
detector = cv2.CascadeClassifier(cascade_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eyes = detector.detectMultiScale(gray, 1.1, 5)
for x, y, width, height in eyes:
    cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
print("Eyes detected:", len(eyes))
cv2.imshow("Eye Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
