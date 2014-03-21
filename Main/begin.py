#-*- encoding: utf-8 -*-
__author__ = 'better'

import Orange
# 导入测试数据voting.tab
# data = orange.ExampleTable("voting")
filepath = "D:\\t_alibaba_data.csv"
data = Orange.data.Table(filepath)

# 输出
all_data = len(data)

for d in data[:100]:
    print d

