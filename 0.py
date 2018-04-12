# _*_ coding:utf-8 _*_
from PIL import Image
import numpy as np
import pickle
import pickle,glob,os

####首先将第一章图片转换成数组形式存放在outBin当中

infilename = 'haze_test (1).jpg'#将第一个image文件名赋值给变量
imageAA = Image.open(infilename)#通过open方法打开image图片
imageAA = (np.array(imageAA))

#分别获取图像的RGB通道的像素
imageR = imageAA[:,:,0].flatten()
imageG = imageAA[:,:,1].flatten()
imageB = imageAA[:,:,2].flatten()
Hazelabel = [0]#数据集标签
outBin = np.array(list(Hazelabel) + list(imageR) + list(imageG) + list(imageB),np.uint8)#将RGB像素值以及数据集标签传给数组outBin并保存

####通过循环将所有图像的像素以及标签都保存在outBin数组当中
for i in range(28):
    i = i + 2
    j = str(i)
    infilename = 'haze_test (' + j + ').jpg'
    imageAA = Image.open(infilename)
    imageAA = (np.array(imageAA))

    imageR = imageAA[:,:,0].flatten()
    imageG = imageAA[:,:,1].flatten()
    imageB = imageAA[:,:,2].flatten()
    Hazelabel = [0]
    outBin = np.hstack([outBin,np.array(list(Hazelabel) + list(imageR) + list(imageG) + list(imageB),np.uint8)])

####最后写入到二进制文件当中
outBin.tofile("F:\\image2binary\\test_haze_bin.bin")
####如果成功打印success
print("sucess")