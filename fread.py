# -*- coding: utf-8 -*-
# @Author: wang
# @Date:   2018-01-08 15:29:03
# @Last Modified by:   wang
# @Last Modified time: 2018-01-08 15:29:05
def openfile (file):
    #f = open(file, 'r')
    f = open(file, 'a')#a 追加　w重写　r读
    f.write('aaaaaaaaa')
    f.close()
    #del f
    f = open(file, 'r')
    #a = f.read(6)#读取多少字节的内容 str 
    #a = f.tell()#当前文件操作的位置　int
    #a = f.seek(2,1)#移动文件操作的位置　　seek(offset,[form])
    #a = f.tell()
    print f,a,type(a)
openfile('./a.txt')