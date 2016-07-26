#!/usr/bin/python
# -*- coding: utf-8 -*- 
def fn(x):
	for i in range(2,x):
		if x%i==0:
			return True
	else:
		return False

print filter(fn,range(2,100))
