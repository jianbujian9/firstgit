#!/usr/bin/python
# -*- coding: utf-8 -*- 
#可变参数：参数的个数是可变的
#当传进来的是list 或是 tuple时
def my_sum(*numbers):
	sum=0

	for i in numbers:
		sum=sum+i
	print sum
numbers=[1,2,3,4]
#my_sum(1,2,3,4)
my_sum(*numbers)
			
