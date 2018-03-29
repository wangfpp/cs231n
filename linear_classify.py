# -*- coding: utf-8 -*-
# @Author: wangjb
# @Date:   2018-03-22 14:31:40
# @Last Modified by:   wangjb
# @Last Modified time: 2018-03-22 14:31:41
import numpy as np
import math
def lose_score(x,y,w,delta=1.0):
    label = w.shape[0]#有多少分类
    pre_label = w.dot(x)
    correct_label = pre_label[y]
    loss_i = 0.0
    for i in xrange(label):
        if i == y:
            continue
        loss_i += max(0, pre_label[i] - correct_label + delta)
    return loss_i
W = np.array([[0.01,-0.05,0.1,0.05],[0.7,0.2,0.05,0.16],[0.0,-0.45,-0.2,0.03]])
x = np.array([-15,22,-44,56])
b = np.array([0,0.2,-0.3])
y = W.dot(x) + b
Li_loss = max(0,-2.58 - 0.28 + 1) + max(0,0.86 - 0.28 + 1)
f = np.array(y)
p = np.exp(f) / np.sum(np.exp(f))
print f