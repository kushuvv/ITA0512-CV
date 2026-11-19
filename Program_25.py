import cv2

image = cv2.imread("image.jpg")
reference = cv2.imread("watch_reference.jpg")
if image is None or reference is None:
    raise FileNotFoundError("Place image.jpg and watch_reference.jpg in this folder")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_reference = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
orb = cv2.ORB_create(nfeatures=1500)
key1, desc1 = orb.detectAndCompute(gray_reference, None)
key2, desc2 = orb.detectAndCompute(gray_image, None)
if desc1 is None or desc2 is None:
    raise ValueError("Could not find enough features")
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = sorted(matcher.match(desc1, desc2), key=lambda item: item.distance)
result = cv2.drawMatches(reference, key1, image, key2, matches[:30], None, flags=2)
print("Watch reference matches:", len(matches))
cv2.imshow("Watch Recognition", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
