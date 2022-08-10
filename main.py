#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/08/10 11:10:06
@Author  :   ykzhou 
@Version :   0.0
@Contact :   ykzhou@stu.xidian.edu.cn
@Desc    :   None
'''

from random import seed
from Kmeans import Kmeans
import os
import argparse 

parser = argparse.ArgumentParser(description="hyper parameters for kmeans")

parser.add_argument("ImageName",type=str,help="select the image file name, must in the example directory")
parser.add_argument("-k",type=int,default=4,help="number of center")
parser.add_argument("--MaxIter",type=int,default=30,help="max iterations of kmeans algorithm")
parser.add_argument("--seed",type=int,default=0,help="seed for random center")

args = parser.parse_args()

# hyper parameters
imageName = args.ImageName
resultPath = os.getcwd() + '/result'
k = args.k
max_iter = args.MaxIter
seed = args.seed

solutions = Kmeans(k,resultPath,max_iter=max_iter)

if __name__ == "__main__":
    solutions.run(imageName,seed=seed)