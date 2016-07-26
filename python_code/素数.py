#!/usr/bin/python
# -*- coding: utf-8 -*- 
def fn(x):
	if x==1:
		print 1
	else:
		for i in range(2,x):
			a=2
			while a<i:
				if i%a==0:
					break
				a=a+1
			else:
				print i

fn(100)
			
