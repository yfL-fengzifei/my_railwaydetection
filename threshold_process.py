import cv2
import numpy as np

def abs_sobel_thresh(img,orient='x',thresh_min=0,thresh_max=255):
    #转换成灰度图
    gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    #参考代码方法
    #在x和y方向上应用sobel函数
    if orient=='x':
        abs_sobel=np.absolute(cv2.Sobel(gray_img,cv2.CV_64F,1,0))
    if orient=='y':
        abs_sobel=np.absolute(cv2.Sobel(gray_img,cv2.CV_64F,0,1))
    #转换为8位整数
    sobel_img=np.uint8(255*abs_sobel/np.max(abs_sobel))

    # #方法二
    # if orient=='x':
    #     sobel_img=cv2.Sobel(gray_img,-1,1,0)
    # if orient=='y':

    # #方法三
    # if orient=='x':
    #     sobel_img=cv2.Sobel(gray_img,cv2.CV_64F,1,0)
    # if orient=='y':
    #     sobel_img=cv2.Sobel(gray_img,cv2.CV_64F,0,1)
    # #利用内置函数进行转换
    # sobel_img=cv2.convertScaleAbs(sobel_img)

    #创建一个空数组
    binary_img=np.zeros_like(sobel_img)

    #阈值索引
    binary_img[(sobel_img>=thresh_min)&(sobel_img<=thresh_max)]=255 #参考代码中给的是1,我觉得这里应该是255

    return binary_img

def mag_thresh(img,sobel_kernel=3,mag_thresh=(0,255)):
    """
    :param img:
    :param sobel_kernel:
    :param meg_thresh:
    :return:
    """
    gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    #sobel梯度检测
    sobelx_img=cv2.Sobel(gray_img,cv2.CV_64F,1,0,ksize=sobel_kernel)
    sobely_img=cv2.Sobel(gray_img,cv2.CV_64F,0,1,ksize=sobel_kernel)

    #计算梯度幅值
    #参考代码方法
    # grad_mag=np.sqrt(sobelx_img**2+sobely_img**2)
    #使用内置代码
    grad_mag=cv2.magnitude(sobelx_img,sobely_img) #等于参考中的代码

    #归一化到0-255
    #参考代码方法
    scale_factor=np.max(grad_mag)/255
    grad_mag=(grad_mag/scale_factor).astype(np.uint8)
    # #方法二
    # grad_mag=cv2.convertScaleAbs(grad_mag)

    #创建一个空数组
    binary_mag=np.zeros_like(grad_mag)
    binary_mag[(grad_mag>=mag_thresh[0])&(grad_mag<=mag_thresh[1])]=255 #参考代码中给的是1，我觉得应该是255

    return binary_mag


def dir_thresh(img,sobel_kernel=3,dir_thresh=(0,np.pi/2)):
    """
    :param img:
    :param sobel_kernel:
    :param dir_thresh:
    :return:
    """
    gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    #sobel梯度检测
    sobelx_img=cv2.Sobel(gray_img,cv2.CV_64F,1,0,ksize=sobel_kernel)
    sobely_img=cv2.Sobel(gray_img,cv2.CV_64F,0,1,ksize=sobel_kernel)

    #计算梯度方向
    #参考代码
    #为什么要用绝对值,都求绝对值，不就没有象限的概念了吗,(貌似这里不是为了真的计算方向，而是就是保留有方向的像素)
    grad_dir=np.arctan2(np.absolute(sobelx_img),np.absolute(sobelx_img))
    #内置代码
    # grad_dir=cv2.phase(sobelx_img,sobely_img)

    #创建一个空数组
    binary_dir=np.zeros_like(grad_dir)
    binary_dir[(grad_dir>=dir_thresh[0])&(grad_dir<=dir_thresh[1])]=255 #原文代码中给的是1，我觉的应该是255,好像1和255都可以(但是不太一样)

    return binary_dir


def hls_select(img,channel='s',hls_thresh=(0,255)):
    """
    :param img:
    :param thresh:
    :return:
    """
    hls_img=cv2.cvtColor(img,cv2.COLOR_RGB2HLS)
    if channel=='h':
        channel=hls_img[:,:,0]
    elif channel=='l':
        channel=hls_img[:,:,1]
    else:
        channel=hls_img[:,:,2]

    binary_channel=np.zeros_like(channel)
    binary_channel[(channel>=hls_thresh[0])&(channel<=hls_thresh[1])]=255

    return binary_channel


def lab_select(img,lab_thresh=(0,255)):
    """
    :param img:
    :param lab_thresh:
    :return:
    """
    lab_img = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)
    b_channel = lab_img[:,:,2]
    binary_lab = np.zeros_like(b_channel)
    binary_lab[(b_channel > lab_thresh[0]) & (b_channel <= lab_thresh[1])] = 255
    return binary_lab

def luv_select(img,luv_thresh=(0,255)):
    """
    :param img:
    :param luv_thresh:
    :return:
    """
    luv_img = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
    l_channel = luv_img[:,:,0]
    binary_luv = np.zeros_like(l_channel)
    binary_luv[(l_channel > luv_thresh[0]) & (l_channel <= luv_thresh[1])] = 255
    return binary_luv


def thresholding(img):
    """
    :param img:
    :return:
    """
    x_threshold=abs_sobel_thresh(img,orient='x',thresh_min=90,thresh_max=255)
    mag_threshold=mag_thresh(img,sobel_kernel=3,mag_thresh=(30,170))
    dir_threshold=dir_thresh(img,sobel_kernel=3,dir_thresh=(0.7,1.3))
    hls_threshold=hls_select(img,hls_thresh=(160,255)) #通道顺序hls
    lab_threshold=lab_select(img,lab_thresh=(155,210))
    luv_threshold=luv_select(img,luv_thresh=(225,255))

    #综合阈值
    thresh_img=np.zeros_like(x_threshold)
    thresh_img[((x_threshold == 255) & (mag_threshold == 255)) | ((dir_threshold == 255) & (hls_threshold == 255)) | (lab_threshold == 255) | (luv_threshold == 255)]=255

    return thresh_img