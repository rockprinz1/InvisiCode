from PIL import Image, ImageEnhance

# Load image
img = Image.open("t1.jpg")

# Create an ImageEnhance object to adjust contrast
enhancer = ImageEnhance.Contrast(img)

# Increase contrast by a factor of 1.5
img_contrast = enhancer.enhance(10)

# Save the output image
img_contrast.save("t3.jpg")