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
    #在图像的下半部分进行直方图计算,计算每一列的像素值
    #好像利用cv2.calcHist不行
    histogram=np.sum(bird_img[bird_img.shape[0]//2:,:],axis=0)//255
    #除不除以255都无所谓
    # print(histogram)

    #找到直方图左右部分的峰值
    #these will be the strating point for the left and right liines,为什么是左右峰值的起始点？？？
    #把直方图分成两部分
    midpoint=np.int(histogram.shape[0]/2) #中间点
    #分别返回左右两部分中最大值所在的索引(列索引)
    leftx_base=np.argmax(histogram[:midpoint])
    rightx_base=np.argmax(histogram[midpoint:])+midpoint #argmax返回的是索引

    #选择滑窗的数量
    #根据参考代码，其中应该是沿第一维度(列),即图像的高方向分成几个窗口
    nwindows=9
    #设置窗口的高度，纵向分成nwindows个窗口
    window_height=np.int(bird_img.shape[0]/nwindows)
    #identify the x and y positions of all nonzero pixels in the image
    nonzero=bird_img.nonzero() #返回的是非0值的索引,应该是tuple的形式,x索引和y索引
    nonzeroy=np.array(nonzero[0])
    nonzeroyx=np.array(nonzero[1])

    #current positions to be based updated for each window
    #把当前 左右直方图中最大最值的索引取出来，前面说是左右线的起始点
    leftx_current=leftx_base
    rightx_current=rightx_base

    #set the width the windows +- margin
    #设置窗口的宽度的正负偏差
    margin=100

    #set minimum number of pixels found to recenter window
    minpix=50

    #create empty lists to receive left and right lane pixel indices
    left_lane_inds=[]
    right_lane_inds=[]

    #一个一个的遍历窗口
    for window in range(nwindows):
        #窗口边界
        #窗口的上边界
        win_y_low=bird_img.shape[0]-(window+1)*window_height #虽然是low 但其实是上顶边，因为数小
        #窗口的下边界
        win_y_high=bird_img.shape[0]-window*window_height #虽然是high 但其实是下底边，因为数大
        #当前最大(列索引下)
        win_xleft_low=leftx_current-margin
        win_xleft_high=leftx_current+margin
        win_xright_low=rightx_current-margin
        win_xright_high=rightx_current+margin

        #






