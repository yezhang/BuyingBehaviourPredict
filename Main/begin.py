#-*- encoding: utf-8 -*-
__author__ = 'better'

import readData
import cPickle as pickle
from string import *
import Orange
from numpy import *
from numpy.linalg.linalg import *
from scipy import sparse
from scipy.sparse.linalg import *

# 导入测试数据voting.tab
# data = orange.ExampleTable("voting")
filepath = "C:\\Users\\better\\PycharmProjects\\BuyingBehaviourPredict\\data\\t_useritemcount.txt"
data = Orange.data.Table(filepath)

userMap = readData.genUserIdMap()
brandMap = readData.genBrandIdMap()


print "数据长度为%s\n" %(len(data[1:]))
# 构造用户矩阵，用户数884，品牌数9531
# 用户矩阵应为9537×884，为了编程方便，先构造884×9537矩阵
userNum = 884
brandNum = 9531

userMatrix = sparse.csr_matrix((brandNum,userNum))

for d in data[1:]:
    userId = atoi(str(d['user_id']))
    brandId = atoi(str(d['brand_id']))
    clickNum = atoi(str(d['ClickNum']))
    buyNum = atoi(str(d['BuyNum']))
    collectNum = atoi(str(d['CollectNum']))
    cartNUm = atoi(str(d['CartNum']))
    #userRate = str(clickNum)
    userRate = clickNum + buyNum + collectNum + cartNUm

    userIndex = userMap[userId] - 1
    brandIndex = brandMap[brandId] - 1
    # print (userIndex, brandIndex)

    userMatrix[brandIndex, userIndex] = userRate

# pickle.dump(userMatrix, open("D:\\usermatrix.txt", "w"))

U, s, V = svds(userMatrix)
print U
print s
print V



