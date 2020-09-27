import cv2
import numpy as np
import os

from threshold_process import *
from line import *

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
    # cv2.imshow('thresh img',threshold_img)
    # cv2.waitKey(0)

    #bird_img=threshold_img_warped
    bird_img=cv2.warpPerspective(threshold_img,M,img.shape[1::-1],flags=cv2.INTER_LINEAR) #[n::-1]的用法是从下标n开始反转读取
    # cv2.namedWindow('bird view img',cv2.WINDOW_NORMAL)
    # cv2.imshow('bird view img',bird_img)
    # cv2.imwrite('./data_images/bird_view.jpg',bird_img)
    # cv2.waitKey(0)

    # if left_line.detected and right_line.detected:
    #     pass
    # else:
    #     left_fit,right_fit,left_lane_inds,right_lane_inds=find_line(bird_img)
    # find_line(bird_img)
    print('pass')

