#-*- encoding: utf-8 -*-
__author__ = 'better'

import Orange
from numpy import *
from numpy.linalg.linalg import *

# 导入测试数据voting.tab
# data = orange.ExampleTable("voting")
filepath = "C:\\Users\\better\\PycharmProjects\\BuyingBehaviourPredict\\data\\t_useritemcount.txt"
#data = Orange.data.Table(filepath)

# 输出
#all_data = len(data)
#print all_data




# 构造用户矩阵，用户数884，品牌数9531
# 用户矩阵应为9537×884，为了编程方便，先构造884×9537矩阵
userNum = 884
brandNum = 9531

userMatrix = zeros((userNum,brandNum))
#print userMatrix
userMatrix = matrix('1,2,3;4,5,6')
# userMatrix = zeros((2,3))

# U, s, V = svd(userMatrix, full_matrices=True)
# print U
# print s
# print V



