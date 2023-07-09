import cv2

def apply_cartoon_effect(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to enhance edges and reduce noise
    color = cv2.bilateralFilter(image, 9, 250, 250)

    # Combine edges and color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# Load the image
image_path = 'v1.jpg' #change image file name
image = cv2.imread(image_path)

# Apply cartoon effect
cartoon_image = apply_cartoon_effect(image)

# Display the original and cartoonized images
cv2.imshow('Original Image', image)
cv2.imshow('Cartoonized Image', cartoon_image)
cv2.waitKey(0)
#cv2.destroyAllWindows()
