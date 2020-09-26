import cv2
import numpy as np

#=====================================================逆透视变换
# src_img=cv2.imread('./data_images/385.jpg')
# cv2.imshow('original',src_img)

#float,只能用int
# points=np.float32([[(600, 1080), (850, 300), (1600, 1080), (1000, 300)]])
#点按顺序绘制
#左上角开始，横轴是x,纵轴是Y
# points=np.int32([[(600, 1080), (850, 300), (1000, 300), (1600, 1080)]])
# src_img=cv2.polylines(src_img,points,isClosed=True,color=(255,255,255))
# cv2.imshow('src',src_img)
# cv2.waitKey(0)

# dstpoints=np.int32([[(600, 1080), (600, 0), (1600, 0), (1600, 1080)]])
# src_img=cv2.polylines(src_img,dstpoints,isClosed=True,color=(255,255,255))
# cv2.imshow('src',src_img)

# src_img=cv2.fillPoly(src_img,points,(255,255,255))
# cv2.imshow('fill img',src_img)
# cv2.waitKey(0)

# roi_img=src_img[300:1080,600:1600,:]
# cv2.imshow('roi img',roi_img)
# cv2.waitKey(0)

# points=points.astype(np.float32)
# dstpoints=dstpoints.astype(np.float32)
# M=cv2.getPerspectiveTransform(np.float32(points),np.float32(dstpoints))
# dst_img=cv2.warpPerspective(src_img,M,dsize=src_img.shape[1::-1])
# cv2.imshow('dst',dst_img)
# cv2.waitKey(0)
# print('pass')

# Minv=cv2.getPerspectiveTransform(np.float32(dstpoints),np.float32(points))
# dstimginv=cv2.warpPerspective(dst_img,Minv,dsize=(1920,1080))
# cv2.imshow('dst inv',dstimginv)
# cv2.waitKey(0)

#=====================================================sobel测试
# src_img=cv2.imread('./data_images/385.jpg')
# # cv2.imshow('src',src_img)
# gray_img=cv2.cvtColor(src_img,cv2.COLOR_RGB2GRAY)
# # cv2.imshow('gray',gray_img)
# sobel_img=cv2.Sobel(gray_img,cv2.CV_64F,1,0)
# # sobel_img=cv2.Sobel(gray_img,-1,1,0)
# # sobel_img=cv2.Sobel(gray_img,-1,0,1)
# # cv2.imshow('soble',sobel_img)
# # cv2.imshow('sobel 2',cv2.Sobel(gray_img,-1,1,0))
# sobel_imginv=cv2.convertScaleAbs(sobel_img)
# cv2.imshow('sobel inv',sobel_imginv)
#
# # abs_sobel=np.absolute(sobel_img)
# # scaled_sobel=np.uint8(255*abs_sobel/np.max(abs_sobel))
# # cv2.imshow('scaled',scaled_sobel)
#
# binary_img=np.zeros_like(sobel_imginv)
# print('pass')
# binary_img[(sobel_imginv>=90)&(sobel_imginv<=280)]=255 #参考代码给的是1 我觉得是255
# cv2.imshow('binary',binary_img)

#=====================================================梯度幅值、方向计算测试
# src_img=cv2.imread('./data_images/385.jpg')
# gry_img=cv2.cvtColor(src_img,cv2.COLOR_RGB2GRAY)
# sobelx=cv2.Sobel(gry_img,cv2.CV_64F,1,0)
# sobely=cv2.Sobel(gry_img,cv2.CV_64F,0,1)
# grad_meg=np.sqrt(sobelx**2+sobely**2)
# grad_meg2=cv2.magnitude(sobelx,sobely)
#
# grad_meg3=cv2.convertScaleAbs(grad_meg2)
# factor=np.max(grad_meg2)/255
# grad_mag4=(grad_meg2/factor).astype(np.uint8)
#
# binary_mag = np.zeros_like(grad_mag4)
# binary_mag2 = np.zeros_like(grad_mag4)
# binary_mag[(grad_mag4 >= 30) & (grad_mag4 <= 170)] = 255  # 参考代码中给的是1，我觉得应该是255
# binary_mag2[(grad_mag4 >= 30) & (grad_mag4 <= 170)] = 1  # 参考代码中给的是1，我觉得应该是255
# # cv2.imshow('meg',grad_meg3)
# # cv2.imshow('meg2',grad_mag4)
# cv2.imshow('bin mag',binary_mag)
# cv2.imshow('bin mag2',binary_mag2)
#
#
#
# # grad_dir=cv2.phase(sobelx,sobely)
# # grad_dir2=cv2.phase(np.absolute(sobelx),np.absolute(sobely))
# absgraddir=np.arctan2(np.absolute(sobely),np.absolute(sobelx))
# binary_dir=np.zeros_like(absgraddir)
# binary_dir2=np.zeros_like(absgraddir)
# binary_dir[(absgraddir>=0.7)&(absgraddir<=1.3)]=255
# binary_dir2[(absgraddir>=0.7)&(absgraddir<=1.3)]=1
#
# # cv2.imshow('dir',binary_dir)
# # cv2.imshow('dir2',binary_dir2)
# # cv2.imshow('grad',grad_meg2)
#
# # bin=np.zeros((100,100))
# # bin2=np.zeros((100,100))
# # bin[0:50,:]=1
# # bin2[0:50,:]=255
# #
# # cv2.imshow('1',bin)
# # cv2.imshow('2',bin2)

#=====================================================颜色空间
# src_img=cv2.imread('./data_images/385.jpg')
# # hls_img=cv2.cvtColor(src_img,cv2.COLOR_RGB2HLS)
# # # cv2.imshow('hls',hls_img)
# # channel=hls_img[:,:,2]
# # # cv2.imshow('s',channel)
# # binary_hls=np.zeros_like(channel)
# # binary_hls[(channel>=160)]=255
# # cv2.imshow('bin hls',binary_hls)
#
# lab_img = cv2.cvtColor(src_img, cv2.COLOR_RGB2Lab)
# # cv2.imshow('lab',lab_img)
# b_channel = lab_img[:, :, 2]
# # cv2.imshow('lab_b',b_channel)
#
# binary_lab = np.zeros_like(b_channel)
# binary_lab[(b_channel > 130) & (b_channel <= 210)] = 255
# cv2.imshow('bin lab',binary_lab)
#
#
# cv2.waitKey(0)


print('pass')






