import cv2

capture = cv2.VideoCapture("video.mp4")
if not capture.isOpened():
    raise FileNotFoundError("Place video.mp4 in this folder")
fps = capture.get(cv2.CAP_PROP_FPS)
fps = fps if fps > 0 else 20
frames = []
while True:
    success, frame = capture.read()
    if not success:
        break
    frames.append(frame)
capture.release()
if not frames:
    raise ValueError("No frames found")
height, width = frames[0].shape[:2]
writer = cv2.VideoWriter("reverse_slow_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), max(1, int(fps / 3)), (width, height))
for frame in reversed(frames):
    writer.write(frame)
writer.release()
