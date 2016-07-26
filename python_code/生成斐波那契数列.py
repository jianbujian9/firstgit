#!/usr/bin/python
# -*- coding: utf-8 -*- 
#斐波那契数列
def fib(n):
	a,b=0,1
	while a<n:
		print a,
		a,b=b,a+b

fib(2000)
