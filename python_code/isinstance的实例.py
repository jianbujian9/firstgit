#!/usr/bin/python
# -*- coding: utf-8 -*- 
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bas operand type')
	if x<0:
		pass
	else:
		return x	

print my_abs('3')
