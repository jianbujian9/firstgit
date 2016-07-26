#!/usr/bin/python
# -*- coding: utf-8 -*- 
#高阶函数filter，将函数作用于一个序列中的每一个元素，返回的是True则保留，False则丢弃

def judge(n):
	return n%2==1

l=[1,2,3,4,5,6,7,8,9]

print filter(judge,l)
