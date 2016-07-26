#!/usr/bin/python
# -*- coding: utf-8 -*- 
#关键字参数：允许传入0个或者任意个带有参数名的参数，这些关键字参数在函数内部自动组装成一个dict
def message(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw

message('xiaoming',39,city='beijing',sex='man')
