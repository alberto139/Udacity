import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#import cv2

# Read in the image and print out some stats
image = mpimg.imread('test.jpg')
print('This image is: ',type(image), 
         'with dimensions:', image.shape)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)

# Define our color selection criteria
# Note: if you run this code, you'll find these are not sensible values!!
# But you'll get a chance to play with them soon in a quiz
red_threshold = 220
green_threshold = 220
blue_threshold = 220
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# Identify pixels below the threshold
thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])

color_select[thresholds] = [0,0,0]

# Display the image    
fig = plt.figure()
a=fig.add_subplot(2,1,1)
plt.title("Original")
plt.imshow(image) 

a=fig.add_subplot(2,1,2)
plt.title("Test")
plt.imshow(color_select)

plt.show()  

mpimg.imsave("test-after.jpg", color_select)
