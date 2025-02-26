# Data Hiding in images using steganography
This is a simple python code which implements the basic concept of steganography, allowing the user to hide text inside images.

# Requirements
Make sure the following are installed:
1. Python
2. OpenCV python library

# Usage
In order to use the program, first, either edit the code to include proper image path or place the image in same folder as the python file, rename it to "Source_image.png", then run the code.
When prompted, enter the text to hide and the password.

# Features
Implements basic steganography, allowing user to hide text inside images.
allows password protected resulting file, which opens normally, but requires passowrd to reveal hidden text.
Hides the text by modyfying the LSB of color values of the pixels of image in use.

# Limitations & improvements
Since it is the basic implementation, it has limited features. Following are the limitations of the project, which can be improved as per need:
It does not use any cryptographic measures to encrypt the text or password.
It does not have a GUI, hence not suitable for everyone.
It is limited to images only.
The text size is limited by the pixels of image.
