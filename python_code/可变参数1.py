#!/usr/bin/python
# -*- coding: utf-8 -*- 
#可变参数：参数的个数是可变的
def my_sum(*numbers):
	sum=0

	for i in numbers:
		sum=sum+i
	print sum
my_sum(1,2,3,4)
			
