# -*- coding: utf-8 -*-
 # @Author: wangfpp 
 # @Date: 2018-03-28 10:18:43 
 # @Last Modified by:   wang
 # @Last Modified time: 2018-03-28 10:33:42
 import numpy as np
 def eval_numerical_gradient(f,x):
    fx = f(x)
    h = 0.00001
    grad = np.zeros(x.shape)
    it = np.nditer?(x, flags = ['multi_index'], op_flags=['readwrite'])
    if not it.finished:
        index = it.multi_index
        old_value = x[index]
        x[index] = old_value + h
        fxh = f(x)
        grad[index] = (fxh - fx) / h
        it.iternext()
    return grad