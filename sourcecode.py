# image capture code ___________________________
import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
cam.release()
cv2.destroyAllWindows()
# ---------------till here-------------------------------------

import ColourEqualizer
# import image_processor
import GreyscaleEqualizer



# Histogram equalization is used to enhance the contrast of the image, it
# spreads the intensity values over full range. Histogram equalization
# technique can’t be used for images suffering from non-uniform illumination
# in their backgrounds as this process only adds extra pixels to the light
# regions of the image and removes extra pixels from dark regions of the image
# resulting in a high dynamic range in the output image.The goal of histogram
# equalization is to spread out the contrast of a given image evenly
# throughout the entire available dynamic range.





# Histogram equalization is used to enhance the contrast of the image,
# it spreads the intensity values over full range



# this process only adds extra pixels to the light regions of the image
# and removes extra pixels from dark regions of the image resulting in
# a high dynamic range in the output image.














# # read Image
# img = cv2.imread(img_name)
# rows, cols, ch = img.shape
#
# pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
#
# # M = cv2.getAffineTransform(pts1,pts2)
#
# # Affine Transform
# affine = cv2.warpAffine(img, cv2.getAffineTransform(pts1, pts2), (cols, rows))
#
# # Scaling Image
# scale = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#
# # M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
#
# # Rotation
# rot = cv2.warpAffine(img, cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1), (cols, rows))
#
# # plotting of Output Images
# plt.subplot(141), plt.imshow(img), plt.title('Input')
# plt.subplot(142), plt.imshow(affine), plt.title('Affine Transform')
# plt.subplot(143), plt.imshow(scale), plt.title('scaled')
# # plt.subplot(144), plt.imshow(rot), plt.title('rotated')
# plt.show()

# # contrast enhance
# from PIL import Image, ImageEnhance
# image = Image.open('{}'.format(img_name))
# contrast = ImageEnhance.Contrast(image)
# # plt.subplot(121), plt.imshow(img_name), plt.title('Input')
# # plt.subplot(122), plt.imshow(image), plt.title('output')
# image.show('contrast enhance')
# cv2.waitKey(0)
#
# power transformation
# import cv2
# # import numpy as np
#
# im = cv2.imread('{}'.format(img_name))
# im = im/255.0
# im_power_law_transformation = cv2.pow(im,0.6)
# cv2.imshow('Original Image',im)
# cv2.imshow('output',im_power_law_transformation)
#
# cv2.waitKey(0)
#
# # min- max
# # Apply Min-Max Contrasting
#
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2
# import matplotlib.image as mpimg
#
# # Reading the original image, here 0 implies that image is read as grayscale
# image = cv2.imread('{}'.format(img_name), 0)
# # Create an empty array to store the final output
# image_cs = np.zeros((image.shape[0],image.shape[1]), dtype='uint8')
#
#
#
# min = np.min(image)
# max = np.max(image)
#
# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         image_cs[i,j] = 255*(image[i,j]-min)/(max-min)
#
# # plt.subplot(121), plt.imshow(image_cs), plt.title('output')
# # plt.show()
# cv2.imshow('Min-Max Contrasting',image_cs)
#
# cv2.waitKey(0)