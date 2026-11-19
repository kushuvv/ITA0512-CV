40 Python OpenCV Lab Programs

Each program is saved as a separate Python file.

Required input files:
- image.jpg for image programs
- video.mp4 for video programs
- watch_reference.jpg for Program_25

Install Python packages:
pip install -r requirements.txt

Programs 1-39 use OpenCV and may display windows with cv2.imshow. Run them on a computer with a graphical desktop. Google Colab does not support cv2.imshow directly; use cv2_imshow or adapt the display code for Colab.

Program 25 compares the input image with watch_reference.jpg using ORB feature matching.
Program 28 marks moving foreground objects in a video; it is a basic motion-based detector, not a trained vehicle classifier.
Program 40 also requires the Tesseract OCR application to be installed, in addition to pytesseract.
