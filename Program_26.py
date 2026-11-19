import cv2

capture = cv2.VideoCapture("video.mp4")
if not capture.isOpened():
    raise FileNotFoundError("Place video.mp4 in this folder")
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
fps = 20
writer = cv2.VideoWriter("reverse_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
for frame in reversed(frames):
    writer.write(frame)
writer.release()
