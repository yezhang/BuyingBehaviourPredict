#-*- encoding: utf-8 -*-
__author__ = 'better'

# 给用户ID安排序号
userIdFilePath = "C:\\Users\\better\\PycharmProjects\\BuyingBehaviourPredict\\data\\t_userid.txt"
userIdWithOrderFilePath = "C:\\Users\\better\\PycharmProjects\\BuyingBehaviourPredict\\data\\t_useridordered.txt"
fileHandle = open(userIdFilePath)
filetowrite = open(userIdWithOrderFilePath, 'w+')

fileList = fileHandle.readlines()
index = 0
for line in fileList:
    filetowrite.write(str(index))
    filetowrite.write('\t')
    filetowrite.write(line)
    index += 1

filetowrite.close()
fileHandle.close()

# 给品牌ID安排序号
userIdFilePath = "C:\\Users\\better\\PycharmProjects\\BuyingBehaviourPredict\\data\\t_brandid.txt"
userIdWithOrderFilePath = "C:\\Users\\better\\PycharmProjects\\BuyingBehaviourPredict\\data\\t_brandidordered.txt"
fileHandle = open(userIdFilePath)
filetowrite = open(userIdWithOrderFilePath, 'w+')

fileList = fileHandle.readlines()
index = 0
for line in fileList:
    filetowrite.write(str(index))
    filetowrite.write('\t')
    filetowrite.write(line)
    index += 1

filetowrite.close()
fileHandle.close()