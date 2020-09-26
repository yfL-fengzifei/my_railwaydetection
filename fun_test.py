import cv2
import numpy as np

#=====================================================逆透视变换
# src_img=cv2.imread('./data_images/385.jpg')
# # cv2.imshow('original',src_img)
#
# #float,只能用int
# # points=np.float32([[(600, 1080), (850, 300), (1600, 1080), (1000, 300)]])
# #点按顺序绘制
# #左上角开始，横轴是x,纵轴是Y
# points=np.int32([[(600, 1080), (850, 300), (1000, 300), (1600, 1080)]])
# src_img=cv2.polylines(src_img,points,isClosed=True,color=(255,255,255))
# # cv2.imshow('src',src_img)
# # cv2.waitKey(0)
#
# dstpoints=np.int32([[(600, 1080), (600, 0), (1600, 0), (1600, 1080)]])
# # src_img=cv2.polylines(src_img,dstpoints,isClosed=True,color=(255,255,255))
# # cv2.imshow('src',src_img)
# # cv2.waitKey(0)
#
# # src_img=cv2.fillPoly(src_img,points,(255,255,255))
# # cv2.imshow('fill img',src_img)
#
# # roi_img=src_img[300:1080,600:1600,:]
# # cv2.imshow('roi img',roi_img)
# # cv2.waitKey(0)
#
# points=points.astype(np.float32)
# dstpoints=dstpoints.astype(np.float32)
# M=cv2.getPerspectiveTransform(np.float32(points),np.float32(dstpoints))
# dst_img=cv2.warpPerspective(src_img,M,dsize=(1920,1080))
# # cv2.imshow('dst',dst_img)
# # cv2.waitKey(0)
#
# Minv=cv2.getPerspectiveTransform(np.float32(dstpoints),np.float32(points))
# dstimginv=cv2.warpPerspective(dst_img,Minv,dsize=(1920,1080))
# cv2.imshow('dst inv',dstimginv)
# cv2.waitKey(0)

#=====================================================sobel测试
src_img=cv2.imread('./data_images/385.jpg')
# cv2.imshow('src',src_img)
gray_img=cv2.cvtColor(src_img,cv2.COLOR_RGB2GRAY)
cv2.imshow('gray',gray_img)

cv2.waitKey(0)
print('pass')






