#!/usr/bin/python
# -*- coding: utf-8 -*- 
def person(a,b,c,*age,**city):
	print a,b,c,age,city

age=[1,3,5,5,6,2]
person(*age,city="beijing")
