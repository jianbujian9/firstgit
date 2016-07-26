#!/usr/bin/python
# -*- coding: utf-8 -*- 
print u'你好，冒险者，我是穆，你是？' 
name=raw_input(u'你的名字：'.encode('utf-8'))
print u'%s,你好，真是个好名字，欢迎来到%s' %(name.decode('utf-8'),u'法兰城')

# str->decode()->unicode
# unicode->encode()->str
