# -*- coding: utf-8 -*-
import os
def ospath(path_filename):
  # a = os.listdir(path_filename)#os.listdir()返回一个ｌｉｓｔ　包含当前目录下的所有文件
  # for i in xrange (len(a)):
  #   print a[i]
  
  # a = os.getcwd()#返回当前完整的工作目录　str 'work/study'
  # print type(a),a

  # a = os.curdir #返回当前目录　str 　　.
  # print type(a),a

  # os.chdir(path_filename)#改变工作目录到　path_filename
  # a = os.getcwd()
  # print type(a) , a
  # print os.listdir(a)

  #a = os.path.isdir(path_filename) #判断是否是一个目录 bool 

  #a = os.path.isfile(path_filename) #判断是否是一个文件 bool

  #a = os.path.exists(path_filename) #判断是否存在文件或目录 bool

  #a = os.path.getsize(path_filename) #返回目录文件的大小　以字节为单位　int
  
  #a = os.path.abspath(path_filename) #获得path_filename的绝对路径　str
  
  #a = os.path.normpath(path_filename) #规范path_filename字符串形式 str
  
  #a = os.path.split(path_filename)　#分割文件和目录 tuple
  
  #a = os.path.splitext(path_filename) #分离文件名与扩展名 tuple

  #a = os.path.join(path_filename, 'python') #链接目录与文件名或目录(返回一个完整的目录)　str
  
  #a = os.path.basename(path_filename) #返回文件名　　没有文件返回空　str

  #a = os.path.dirname(path_filename) #返回文件路径　str
  
  
  
  print type(a), a
ospath('../study/')
