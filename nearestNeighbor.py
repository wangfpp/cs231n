# -*- coding: utf-8 -*-
# @Author: wang
# @Date:   2017-12-26 17:35:00
# @Last Modified by:   wang
# @Last Modified time: 2017-12-26 17:37:18
import numpy as np
from loadFile import load_CIFAR10 #form  file   import  function
Xtr, Ytr, Xte, Yte = load_CIFAR10('cifar-10-batches-py/file/')
#numpy shape  计算出数据的形状　(行,列)
#numpy reshape 重组数据　但是总数要保持不变
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3)
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3)


class NearestNeighbor (object):
      def __init__(self):#初始化类
        pass
      def train(self, X, Y):#训练函数
        self.Xtr = X
        self.Ytr = Y
      def predict (self, X):#预测
        num_test = X.shape[0]
        Ypred = np.zeros(num_test, dtype = self.Ytr.dtype)
        for i in xrange (num_test):
          distances = np.sum(np.abs(self.Xtr - X[i, :]), axis = 1)
          min_index = np.argmin(distances)
          Ypred[i] = self.Ytr[min_index]
        print Ypred
        return Ypred

if __name__ == '__main__':
  nn = NearestNeighbor()
  nn.train(Xtr_rows, Ytr)
  Yte_predict = nn.predict(Xte_rows)
  print 'accuracy: %f' % ( np.mean(Yte_predict == Yte) )
  		
    		
    		
    		
		