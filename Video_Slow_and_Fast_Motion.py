import cv2

capture = cv2.VideoCapture("video.mp4")
if not capture.isOpened():
    raise FileNotFoundError("Place video.mp4 in this folder")
fps = capture.get(cv2.CAP_PROP_FPS)
delay = max(1, int(1000 / fps)) if fps > 0 else 30
while True:
    success, frame = capture.read()
    if not success:
        break
    cv2.imshow("Normal Speed", frame)
    if cv2.waitKey(delay) & 0xFF == ord("q"):
        break
capture.release()
capture = cv2.VideoCapture("video.mp4")
while True:
    success, frame = capture.read()
    if not success:
        break
    cv2.imshow("Slow Motion", frame)
    if cv2.waitKey(delay * 3) & 0xFF == ord("q"):
        break
capture.release()
capture = cv2.VideoCapture("video.mp4")
while True:
    success, frame = capture.read()
    if not success:
        break
    cv2.imshow("Fast Motion", frame)
    if cv2.waitKey(max(1, delay // 3)) & 0xFF == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()
