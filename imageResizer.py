import cv2

source_name = input("Enter the name of your image (along with the extension): ")
final_name = input("Enter the name you wish for the resized image: ")
scale_percent = int(input("Enter the scale percentage for the image: "))

# first the path, then the method so that the image is represented as it is
image = cv2.imread(source_name, cv2.IMREAD_UNCHANGED)

# title and then the source
cv2.imshow("Shameer", image)


# calculate the scale percentage of the image
NEW_WIDTH = int(image.shape[1] * (scale_percent / 100))
NEW_HEIGHT = int(image.shape[0] * (scale_percent / 100))

# resizing the image
output = cv2.resize(image, (NEW_WIDTH, NEW_HEIGHT))

cv2.imwrite(final_name, output)

# waits for a key to be pressed
cv2.waitKey(0)
