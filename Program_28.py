import cv2

capture = cv2.VideoCapture("video.mp4")
if not capture.isOpened():
    raise FileNotFoundError("Place video.mp4 in this folder")
background = cv2.createBackgroundSubtractorMOG2()
while True:
    success, frame = capture.read()
    if not success:
        break
    mask = background.apply(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, width, height = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
    cv2.imshow("Moving Object Detection", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()
