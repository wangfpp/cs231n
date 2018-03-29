# -*- coding: utf-8 -*-
# @Author: wang
# @Date:   2017-12-26 17:45:59
# @Last Modified by:   wang
# @Last Modified time: 2017-12-26 17:46:13
#加载文件
import numpy as np
import os#路径
import pickle#序列化和反序列化
def load_CIFAR10(ROOT):#加载所有数据(训练集和测试集)　需要零次调用　pickle
    """ load all of cifar """
    xs = []
    ys = []
    for b in range(1,6):#rang xrang
      f = os.path.join(ROOT, 'data_batch_%d' % (b, ))#os.path.join()返回一个完整的目录
      X, Y = load_CIFAR_batch(f)#调用函数
      xs.append(X)#append 插入到list尾部
      ys.append(Y)    
    Xtr = np.concatenate(xs)#使变成行向量 拼接数组　concat()
    Ytr = np.concatenate(ys)
    #Xtr Ytr训练集数据 图片个标签
    del X, Y#删除变量　　数据还存在
    Xte, Yte = load_CIFAR_batch(os.path.join(ROOT, 'test_batch'))#测试集数据
    print Xtr,Ytr
    return Xtr, Ytr, Xte, Yte#训练集数据和测试集数据一并返回
def load_CIFAR_batch(filename):#加载数据源
   """ load single batch of cifar """
   with open(filename, 'rb') as f:
     datadict = pickle.load(f)
     X = datadict['data']
     Y = datadict['labels']
     X = X.reshape(10000, 3, 32,32).transpose(0,2,3,1).astype("float")
     Y = np.array(Y)
     return X, Y
