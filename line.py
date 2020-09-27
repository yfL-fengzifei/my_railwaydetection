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
        self.best_fit=None
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

    def check_detected(self):
        """
        :return:
        """
        pass

    def update(self,fit):
        """
        :param fit:
        :return:
        """
        if fit is not None:
            if self.best_fit is not None: #初始化的时候 best_fit=None,即第一次计算之后，直接执行else
                self.diffs=abs(fit-self.best_fut)
                pass
            else:
                self.best_fit=fit
                self.current_fit=fit
                self.detected=True
                self.recent_fitted.append(fit)


def find_line(bird_img):
    """
    :param bird_img:
    :return:
    """
    #在图像的下半部分进行直方图计算,计算每一列的像素值
    #好像利用cv2.calcHist不行
    histogram=np.sum(bird_img[bird_img.shape[0]//2:,:],axis=0)
    #除不除以255都无所谓
    # print(histogram)

    #找到直方图左右部分的峰值
    #these will be the strating point for the left and right liines,为什么是左右峰值的起始点...？？？...
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
    #tuple中的每个元素 中包含的元素数是一样的
    nonzeroy=np.array(nonzero[0]) #第几行
    nonzerox=np.array(nonzero[1]) #第几列

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

    #一个一个的遍历窗口,这里的窗口是沿着图像高度分成几个窗口
    for window in range(nwindows):
        #定义窗口边界，上下左右
        #窗口的上边界
        win_y_low=bird_img.shape[0]-(window+1)*window_height #虽然是low 但其实是上顶边，因为数小
        #窗口的下边界
        win_y_high=bird_img.shape[0]-window*window_height #虽然是high 但其实是下底边，因为数大

        #当前最大(列索引下)
        #_current为当前峰值的索引
        #左半线
        win_xleft_low=leftx_current-margin #左边界
        win_xleft_high=leftx_current+margin #右边界
        #右半线
        win_xright_low=rightx_current-margin #左边界
        win_xright_high=rightx_current+margin #右边界

        #identify the nonzero pixels in x and y with the window
        #nonzeroy 为bird_img所有非零元素的索引的y值
        #计算的是左窗口下满足要求的非零值索引
        #对应于左轨道
        good_left_inds=((nonzeroy>=win_y_low)&(nonzeroy<win_y_high)&(nonzerox>=win_xleft_low)&(nonzerox<win_xleft_high)).nonzero()[0] #返回的是ndarray,每个元素对应的是满足要求的索引号

        #计算的是右窗口下满足要求的非零值索引
        #对应于右轨道
        good_right_inds=((nonzeroy>=win_y_low)&(nonzeroy<win_y_high)&(nonzerox>=win_xright_low)&(nonzerox<win_xright_high)).nonzero()[0] #返回的是ndarray,值得注意的是ndarray也可以使用len，每个元素对应的是满足要求的索引号

        #将这些索引添加到list中
        left_lane_inds.append(good_left_inds)
        right_lane_inds.append(good_right_inds)

        #if you find > minpix pixels, recenter next window on their mean position
        #当满足条件的时候，重新赋值当前列(左右列)
        if len(good_left_inds)>minpix:
            leftx_current=np.int(np.mean(nonzerox[good_left_inds])) #mean求平均值，重新赋值左列
        if len(good_right_inds)>minpix:
            rightx_current=np.int(np.mean(nonzerox[good_right_inds])) #重新赋值右列

        #在for循环里保留了，当前窗口下的good_X_inds
        #然后更新了当前的搜索列位置

    #concatenate the arrays of indices
    #默认拼接维度为axis=0
    #有重复的怎么办 ...???...,(已解决)，有重复的也不怕就是要拟合，相当于在一个二维平面上有很多点，要对这些点拟合成一条曲线
    left_lane_inds=np.concatenate(left_lane_inds)
    right_lane_inds=np.concatenate(right_lane_inds)

    #提取位置
    leftx=nonzerox[left_lane_inds]
    lefty=nonzeroy[left_lane_inds]
    rightx=nonzerox[right_lane_inds]
    righty=nonzeroy[right_lane_inds]

    print('pass')

    #利用三阶多项式拟合
    left_fit=np.polyfit(lefty,leftx,3)
    right_fit=np.polyfit(righty,rightx,3) #因为y是行，x列

    return left_fit,right_fit,left_lane_inds,right_lane_inds

def find_line_by_previous(bird_img,left_fit,right_fit):
    """
    :param bird_img:
    :param left_fit:
    :param right_fit:
    :return:
    """
    #返回非零值
    nonzero=bird_img.nonzero() #tuple
    nonzeroy=np.array(nonzero[0]) #其实加不加np.array进行转换都行,第几行
    nonzerox=np.array(nonzero[1]) #第几列

    #设置窗口正负偏差
    margin=100

    #
    # left_lane_inds=((nonzerox>le))
    pass






