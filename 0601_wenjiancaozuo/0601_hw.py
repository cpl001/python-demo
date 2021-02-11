"""
1、有以下数据来自于一个嵌套字典的列表（可自定义这个列表），格式如下：
person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,  .... 其他]


1)创建一个txt文本文件，来添加数据
a.第一行添加如下内容：
name,age,gender,hobby,motto
"""
f = open(r'D:\pycharm\pythonProject\0601_wenjiancaozuo\0601_hw.txt','w',encoding='utf-8')
f.write('name,age,gender,hobby,motto\n')
f.close()


f = open(r'D:\pycharm\pythonProject\0601_wenjiancaozuo\0601_hw.txt','a',encoding='utf-8')
f.write('yuze,17,男,假正经, I am yours')
f.write('\ncainiao,18,女,看书,Lemon is best!')
f.close()