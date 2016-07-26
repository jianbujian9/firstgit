#!/usr/bin/python
# -*- coding: utf-8 -*- 
#关键字参数：允许传入0个或者任意个带有参数名的参数，这些关键字参数在函数内部自动组装成一个dict
#和可变参数类似，可以显组装一个dict,然后将这个dict转换为关键字参数传进去
def message(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw

kw={'city':'beijig','sex':'man'}
#message('xiaoming',39,city='beijing',sex='man')
message('xiaoming',23,**kw)
