import cv2

image = cv2.imread("image.jpg")
if image is None:
    raise FileNotFoundError("Place image.jpg in this folder")
cascade_path = cv2.data.haarcascades + "haarcascade_smile.xml"
detector = cv2.CascadeClassifier(cascade_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
smiles = detector.detectMultiScale(gray, 1.7, 20)
for x, y, width, height in smiles:
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
print("Smiles detected:", len(smiles))
cv2.imshow("Smile Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
