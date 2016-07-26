#!/usr/bin/python
# -*- coding: utf-8 -*- 
#默认参数 
def power(x,n=2):
	sum=1
	while n>0:
		sum=sum*x
		n=n-1
	print sum

power(3,6)
