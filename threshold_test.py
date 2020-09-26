import numpy as np
import cv2
import utils

def thresholding(img):
    #setting all sorts of thresholds
    x_thresh = utils.abs_sobel_thresh(img, orient='x', thresh_min=90 ,thresh_max=280)
    mag_thresh = utils.mag_thresh(img, sobel_kernel=3, mag_thresh=(30, 170))
    dir_thresh = utils.dir_threshold(img, sobel_kernel=3, thresh=(0.7, 1.3))
    hls_thresh = utils.hls_select(img, thresh=(160, 255))
    lab_thresh = utils.lab_select(img, thresh=(155, 210))
    luv_thresh = utils.luv_select(img, thresh=(225, 255))

    #Thresholding combination
    threshholded = np.zeros_like(x_thresh)
    threshholded[((x_thresh == 1) & (mag_thresh == 1)) | ((dir_thresh == 1) & (hls_thresh == 1)) | (lab_thresh == 1) | (luv_thresh == 1)] = 1

    return threshholded*255

if __name__=="__main__":
    src=cv2.imread('./data_images/385.jpg')
    cv2.imshow('original',src)
    dst=thresholding(src)
    cv2.imshow('dst',dst)
    cv2.waitKey(0)