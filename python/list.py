#!/usr/bin/python
# -*- coding: utf-8 -*-
a = [5,2,3,4]#汉字
#print a
num = [{'Adam' : 95.5},{'Lias' : 85},{'Bart' : 59}]
if num[2] == num[-1]:
    num.append({'Bolo':100})#插到数组的尾部
    #print num
# for i in num:
#     for key in i:
#         #print i[key]
#         if i[key] >= 100:
#             #print i
#             num.insert(0,i)
# print num
num.pop(-1)
#num[2] = {'www': 100}
tmp = ''
tmp = num[0]
num[0] = num[2]
num[2] = tmp
print num
