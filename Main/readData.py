#-*- encoding: utf-8 -*-
__author__ = 'better'

def genMap(path):
    fileHandle = open(path)
    # 丢弃首行
    fileHandle.readline()
    userIdMap = {} #新建一个空字典
    while True:
        line = fileHandle.readline()
        if len(line) == 0:
            break
        index, userId = map(int, line.split())
        userIdMap[userId] = index

    fileHandle.close()

    #print userIdMap

    return userIdMap

def genUserIdMap():
    # 读取文件，存入字典中，记录每个userId的索引和brandId的索引
    userIdWithOrderFilePath = "C:\\Users\\better\\PycharmProjects\\BuyingBehaviourPredict\\data\\t_useridordered.txt"
    return genMap(userIdWithOrderFilePath)

def genBrandIdMap():
    userIdWithOrderFilePath = "C:\\Users\\better\\PycharmProjects\\BuyingBehaviourPredict\\data\\t_brandidordered.txt"
    return genMap(userIdWithOrderFilePath)
