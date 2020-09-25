import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import time
def main(imgs):
    #处理图像
    for img in imgs:
        processing(img)


if __name__=="__main__":
    #读取文件
    PATH='./data_images' #数据相对路径
    PATH=os.path.abspath(PATH) #该项目下的绝对路径
    img_names=os.listdir('data_images') #返回的是路径下的列表，所有文件，不管是文件夹还是列表，且是名字
    img_paths=[PATH+'/'+img_name for img_name in img_names] #图像完整路径
    imgs=[cv2.imread(img_path) for img_path in img_paths] #cv2读取的是numpy的格式,imgs[0].shpe=(h,w,c)

    # cv2.namedWindow('original img',cv2.WINDOW_AUTOSIZE)
    for img in imgs:
        cv2.imshow('original img',img)
        #time.sleep(5)
        cv2.waitKey(1000) #按顺序显示

    main(imgs)

    print('pass')
    #main()