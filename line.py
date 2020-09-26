import numpy as np

class line():
    def __init__(self):
        #was the line detected in the last iteration?
        #在最后一些迭代中是否检测
        self.detected=False
        #x values of the last n fits of the line
        self.recent_fitted=[np.array([False])]
        #average x values of the fitted line over the last n iterations
        self.bestx=None
        #polynomial coefficients for the most recent fit
        self.current_fit=[np.array([False])]
        #radius of curvature of the line in some units
        self.radius_of_curvature=None
        #distance in meters of vehicle center from the line
        self.line_base_pos=None
        #difference in fit cofficients between last and new fits
        self.diffs=np.array([0,0,0,0],dtype='float')
        #x value for detected line pixels
        self.allx=None
        #y value for detected line pixels
        self.ally=None


def find_line(bird_img):
    """
    :param bird_img:
    :return:
    """
    #在图像的下半部分进行直方图计算
    histogram=np.sum(bird_img[bird_img.shape[0]//2:,:],axis=0)//255
    # print(histogram)

    #找到直方图左右部分的峰值
    #these will be the strating point for the left and right liines
    midpoint=np.int(histogram.shape[0]/2)
    leftx_base=np.argmax(histogram[:midpoint])
    rightx_base=np.argmax(histogram[midpoint:])+midpoint #argmax返回的是索引

    #选择滑窗的数量
    nwindows=9
    #设置窗口的高度
    window_height=np.int(bird_img.shape[0]/nwindows)
    #identify the x and y positions of all nonzero pixels in the image

    nonzero=bird_img.nonzero() #返回的是非0值的索引
    nonzeroy=np.array(nonzero[0])
    nonzeroyx=np.array(nonzero[1])

    #current positions to be based updated for each window
    leftx_current=leftx_base
    rightx_current=rightx_base

    #set the width the windows +- margin
    margin=100

    #set minimum number of pixels found to recenter window
    minpix=50

    #create empty lists to receive left and right lane pixel indices
    left_lane_inds=[]
    right_lane_inds=[]

    #一个一个的遍历窗口
    for window in range(nwindows):
        pass




