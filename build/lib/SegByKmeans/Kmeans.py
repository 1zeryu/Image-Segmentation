#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Kmeans.py
@Time    :   2022/08/10 11:10:16
@Author  :   ykzhou 
@Version :   0.0
@Contact :   ykzhou@stu.xidian.edu.cn
@Desc    :   None
'''

from sys import flags
import numpy as np
import cv2 
import os

# The role of this class is to call the Kmeans algorithm on the image
class Kmeans(object):
    def __init__(self, k, resultPath, max_iter=25):
        self.k = k
        self.resultPath = resultPath
        self.max_iter = max_iter
        self.flags = cv2.KMEANS_RANDOM_CENTERS
        self.criteria = (cv2.TermCriteria_EPS+cv2.TermCriteria_MAX_ITER,max_iter,0.1)

    def setk(self, k):
        self.k = k
        
    def setResultPath(self, path):
        self.resultPath = path
    
    def readImage(self, imagePath):
        imagePath = os.getcwd() + '/example/' + imagePath
        print("input image...")
        img = cv2.imread(imagePath)

        return img
    
    def model(self, image, seed):
        np.random.seed(seed)
        img = image.reshape((-1, 3)).astype(np.float32)
        r, best, center = cv2.kmeans(img, self.k, None, criteria=self.criteria,
                                        attempts=10, flags=self.flags)
        center = np.uint8(center)
        # print(img[np.where(best==2)[0]])
        for i in range(self.k):
            img[np.where(best==i)[0]] = center[i]
        segmentation_img = img.reshape(image.shape)
        return segmentation_img
    
    def run(self, imageName, seed=0):
        image = self.readImage(imageName)
        result = self.model(image, seed)  
        cv2.imwrite(self.resultPath+'\\'+imageName , result)
        print("Successfully generated")


        