#!/usr/bin/python
# -*- coding: utf-8 -*- 
def product(x,y):
	return x*y

l=[1,2,3,4,5,5]

print reduce(product,l)
