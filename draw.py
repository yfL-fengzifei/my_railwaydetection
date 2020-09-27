import cv2
import numpy as np

def draw_area(pil_img,bird_img,Minv,left_fit,right_fit):
    """
    :param pil_img:
    :param bird_img:
    :param Minv:
    :param left_fit:
    :param right_fit:
    :return:
    """
    #为画图，生成x,y值
    ploty=np.linspace(0,bird_img.shape[0]-1,bird_img.shape[0]) #0-1079，一共1080个数
    #左轨道
    left_fitx=left_fit[0]*ploty**3+left_fit[1]*ploty**2+left_fit[2]*ploty+left_fit[3] #left_fit 返回的是多项式系数向量，因为是三阶所以返回的是[0\1\2\3]
    #右轨道
    right_fitx=right_fit[0]*ploty**3+right_fit[1]*ploty**2+right_fit[2]*ploty+right_fit[3]

    #创建图像，在其上画图
    bird_img_zero=np.zeros_like(bird_img).astype(np.uint8)
    #其实上就是创建三通道，肯定还有其他方法
    color_warp=np.dstack((bird_img_zero,bird_img_zero,bird_img_zero)) #(h,w,c)

    #将x\y值转变成有用的形式
    pts_left=np.array([np.transpose(np.vstack([left_fitx,ploty]))]) #transpose 转换维度
    pts_right=np.array([np.flipud(np.transpose(np.vstack([right_fitx,ploty])))]) #为什么还要flipud一下，...(因为要形成整个封闭区域)???...
    # pts=np.hstack((pts_left,pts_right)) #这里不知道有什么问题，感觉不太对
    pts=np.vstack([pts_left,pts_right])

    #显示
    cv2.fillPoly(color_warp,np.int_(pts),(255,255,255))
    cv2.imshow('fill',bird_img_zero)
    cv2.waitKey(0)










