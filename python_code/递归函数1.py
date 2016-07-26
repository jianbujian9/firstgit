#!/usr/bin/python
# -*- coding: utf-8 -*- 
#递归函数
def func(n):
	if n==1:
		return 1
	return n*func(n-1)

print func(5)
