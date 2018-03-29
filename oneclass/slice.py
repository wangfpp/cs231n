#coding:UTF-8#
# from math import sqrt
# nums = range(5)#[0,1,2,3,4]
# #nums[2:4] = [8,9]
# #print nums 应该是 [0,1,8,9,4]
# animals = ['cat' , 'dog', 'pig', 'duck']
# for index , animal in enumerate(animals):#enumerate函数可访问每个元素的指针
# 	break
# 	#print  '######%d: %s' %(index + 1, animal)
# #列表推导:
# squares = [x ** 2 for x in nums]
# #print squares 
# even_squares = [x ** 2 for x in nums if x % 2 == 0]
# #print even_squares
# d = {'cat' : 'cute','dog' : 'furry',}
# #print d['cat']
# #print 'cat' in d 
# #print d.get('monkey','N/A')
# #print d.get('cat','N/A')
# a = {'person' : 2, 'cat' : 4, 'spider' : 8}
# for animal, legs in a.iteritems():
# 	break
# 	#print 'A %s  has %d legs' % (animal,legs)
# b = [0,1,2,3,4,5,6,7,8,9,10]
# even_num_to_square = {x : x ** 2 for x in b if x % 2 == 0}
# #print even_num_to_square
# c = {int(sqrt(x)) for x in range(30)}
# print c
#d = {(x , x + 1) for x in range(10)}
#print d

class Greeter(object):
	#print object
	def __init__(self,name):#形参
		print name
		self.name = name
	def greet(self,loud = False):
		if loud:
			print 'Hello, %s!' % self.name.upper()
		else:
			print 'Hello, %s!' % self.name

g = Greeter('Wangjinbiao')
g.greet()
g.greet(loud=True)








