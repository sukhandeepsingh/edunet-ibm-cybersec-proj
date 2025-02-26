import cv2
import os
import string

use_image = cv2.imread("Source_image.png")
# replace Source_image.png with the actual path of image, or place the image in same folder and rename it accordingly

orig_msg = input("Enter text to hide: ")
password = input("Set password: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(orig_msg)):
    use_image[n, m, z] = d[orig_msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", use_image)
os.system("start encryptedImage.jpg")

message = ""
n = 0
m = 0
z = 0

entered_pass = input("Enter password to decode message: ")
if password == entered_pass:
    for i in range(len(orig_msg)):
        message = message + c[use_image[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Hidden text:", message)
else:
    print("Error! try again")
