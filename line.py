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





