#!/usr/bin/python
# -*- coding: utf-8 -*- 
#sorted高阶函数：排序
def desc(x,y):
	if x<y:
		return 1
	elif x>y:
		return -1
	else:
		return 0
l=[32,52,2,5,52,63,2,77]

print sorted(l,desc)
