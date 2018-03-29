#coding:UTF-8#
import numpy as np #引入numpy库
randomNumber = np.random 
#a = np.array([[1,2,3],[4,5,6]])矩阵是每行长度都相等的数组的集合
#print a
#print type(a)
#print a.shape
#a = np.zeros([3,2])
#print a
#b = np.ones([2,2])
#print b 
#c = np.full([3.3],2)#第一个参数是几维矩阵  第二个参数是有几个元素  第三个参数是矩阵中的数值   默认是Float32
#print c
#d = np.eye(4)
#print d
#e = randomNumber.random([2,3]) * 10
#print e
#a = np.array([[21,3,67,02],[8,43,21,5],[43,56,89,0]])
#bool_idx = (a > 2)#寻找 a矩阵中大于2的值 并返回一个新的包含True False的矩阵[[True,True,True,False],[True,True,True,True],[True,True,True,False]]
#print bool_idx
#print a[bool_idx]#把矩阵中为True的相对应的值取出 然后组成新的数组并返回

#数据类型
#x = np.array([1,2])
#print x.dtype
#y = np.array([1.,2], dtype = np.int64)#只要含有Float浮点数此数组就是Float型 可以通过dtype来指定数组的数据类型
#print y.dtype
#print y

######################-------------------------数组的计算---------------------#######################
x = np.array([[1,2],[3,4]],dtype = np.float64)
y = np.array([[5,6],[7,8]],dtype = np.float64)
#print x + y     
#print np.add(x,y)  加法运算

#print x - y
#print np.subtract(x , y) 减法运算

#print x * y
#print np.multiply(x , y) 乘法运算

#print x / y 
#print np.divide(x ,y)  除法运算


#print np.sqrt(x)  开方
v = np.array([9,10])
w = np.array([11,12])

print v.dot(w)
print np.dot(v,w)
 















