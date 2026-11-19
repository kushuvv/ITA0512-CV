import cv2
import pytesseract

capture = cv2.VideoCapture("video.mp4")
if not capture.isOpened():
    raise FileNotFoundError("Place video.mp4 in this folder")
while True:
    success, frame = capture.read()
    if not success:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    if text.strip():
        print(text.strip())
    cv2.imshow("Video Text Extraction", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()
