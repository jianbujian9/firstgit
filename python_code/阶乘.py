#!/usr/bin/python
# -*- coding: utf-8 -*- 
def aa(m):
	sum=1
	if m==1:
		return m
	else:
		while m>1:	
			sum=sum*m
			m=m-1
		return sum

print aa(1000)
