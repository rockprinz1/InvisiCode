import cv2

# Load the image
img = cv2.imread('Addresscopy.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a QR code detector
detector = cv2.QRCodeDetector()

# Detect the QR code in the image
data, bbox, _ = detector.detectAndDecode(gray)

# If a QR code was detected, crop the image to just the QR code
if bbox is not None:
    qr_code = img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
    
    # Save the cropped QR code image
    cv2.imwrite('t4.jpg', qr_code)
