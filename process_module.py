import cv2
import numpy as np
import os

def get_M_Minv():
    """
    点的设置有问题
    :return:
    """
    src=np.float32([[(600, 1080), (850, 300), (1600, 1080), (1000, 300)]])
    dst=np.float32([[(500, 1080), (0, 0), (1500, 1080), (1300, 0)]])

    M=cv2.getPerspectiveTransform(src,dst)
    Minv=cv2.getPerspectiveTransform(dst,src)
    return M,Minv

def abs_sobel_thresh(img,orient='x',thresh_min=0,thresh_max=255):
    #转换成灰度图
    gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    #在x和y方向上应用sobel函数
    if orient=='x':
        abs_sobel=np.absolute(cv2.Sobel(gray_img,cv2.CV_64F,1,0))
    if orient=='y':
        abs_sobel=np.absolute(cv2.Sobel(gray_img,cv2.CV_64F,0,1))



def thresholding(img):
    """
    :param img:
    :return:
    """
    x_threshold=abs_sobel_thresh=(pass)


def processing(img,M,Minv,left_line,right_line):
    """
    :param img:
    :param M:
    :param Minv:
    :param left_line:
    :param right_line:
    :return:
    """
    threshold_img=thresholding(img)