"""
==================================
Author : "cpl"
Time : 22:20
Data : 2020/06/08
Project : web_study

===================================
"""
#路径处理
import os
"""
获取当前文件的绝对路径：os.path.abspath
"""
#1
res = os.path.abspath("hello_py.py")
print(res)#D:\workspace\web_study\py_module

res = os.path.abspath(".")#也可以用.代替， .代表当前
print(res)#D:\workspace\web_study\py_module

"""
获取当前文件所在目录：os.path.dirname("里面给文件的绝对路径")"""
#2
s = os.path.dirname(res)#res 打印出来的结果就是绝对路径
print(s)

#3
base_dir = os.path.dirname(s)
print(base_dir)

#4 得到项目目录下，另一个文件的绝对路径
# 路金拼接：os.path.join(a,b)
res = os.path.join(base_dir,"hello_py.py")
print(res)

"""魔法路径
__file__:当前文件名  res = os.path.abspath(__file__)

__name__ : 如果"""
print(__file__)