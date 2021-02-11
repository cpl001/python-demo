"""0601 文件操作
==================================
Author : "cpl"
Time : 22:20
Data : 2020/06/08
Project : web_study

===================================
"""
"""py30.txt 文本内容
你好
学校
文件按操作
一起来学习’‘
假"""


fs = open('py30.txt')
#open内置函数,使用fs接收它
#'py30.txt'，是相对路径
fs = open(r'D:\workspace\web_study\class_0601\py30.txt')#绝对路径，r是转义字符

"""
r只读：1文件一定要存在，否者报错；
      2默认为只读模式
w只写：1若文件不存在，会自动创建
        2文件所在的目录一定要存在，否者报错
        3会覆盖原有内容
        4只能写入，不能读取
a追加：1若文件不存在，会自动创建
        2文件所在的目录一定要存在，否则报错
        3若文件存在，则直接在文件末尾，继续追加内容
（不常用，rb，wb，ab）
rb只读：二进制方式读，其他一样，（通常用于打开图片）
wb只写：二进制方式写，其他一样，（通常用于打开图片）
ab追加：  二进制方式追加，其他一样，（通常用于打开图片）    
"""


"""
文件读取：read(),readline(),readlines()
1.read() 读取文件的所有数据。默认从头开始，读取出来为字符串  （常用）
2。readline() 读取一行数据     （非常少用）
3.readlines() 按行读取所有数据。结果为列表，一行为一个成员"""

# fs = open(r'D:\workspace\web_study\class_0601\py30.txt',encoding='utf-8')
# 如果文件里面有中文，需要加encoding='utf-8',否者打印下面的东西会报错
# s = fs.read()#读py30.txt文件中的东西
# print(s)
# s1 = fs.read()
# print('想再读1次：',s1)#再读1次就无法再读

# readline() 读取一行数据
# s2 = fs.readline()
# print(s2)#你好
# s3 = fs.readline()
# print(s3)#调取第2次，就读第2行，以此类推。结果为：学校

# readlines() 按行读取所有数据。结果为列表，一行为一个成员
# s4 = fs.readlines()
# print(s4)#['你好\n', '学校\n', '文件按操作\n', '一起来学习’‘\n', '假']


"""文件写入：write（数据）、writelines（列表）
文件写入数据时，不会自动换行。需要再数据当中，加入换行符\n
1.write(数据） 写入数据
2.writelines（列表） 写入列表当中的每个成员    （不常用）
"""

fs = open(r'D:\workspace\web_study\class_0601\py30.txt','w',encoding='utf-8')
#写入，在路径加了'w'
# 使用了外部的资源，再使用之后都要关闭。   编写规范，
fs.write('这是一个写入的文本内容\n')#w模式  文件覆盖
fs.write('hahahha')
fs.close()#关闭文件，释放资料。   第三方资源。
# 写入后文本内容：
# 这是一个写入的文本内容
# hahahha


"""追加。再原有的文件内容之后，追加新的内容
打开文件的时候，模式为a -append
"""
# fs = open(r'D:\workspace\web_study\class_0601\py30.txt','a',encoding='utf-8')
# #追加 在路径后面加了‘a‘
# fs.write('\n这是追加')
# fs.close()


# 写、追加  如果文件不存在，自动创建
# 如果文件路径不存在，会报错
# fs = open('new_file.txt','a',encoding='utf-8')
# fs.write("我是新的文件！")
# fs.close()


#可读可写   +   r/w     （不常用）
# r+    可读可追加
# w+    先清除内容，在写入
# fs = open("可读可写.txt",encoding='utf-8',mode="rw")
# print(fs.read())
# fs.write('ssssssss')
# fs.close()


"""（较常用 用起来方便）
高逼格小招数：上下文管理器with
使用with操作文件的好处：会启动文件的上下文管理器，不需要关闭文件，会自动关闭文件
"""
with open('new_file.txt','a',encoding='utf-8') as fs:
    fs.write("自动关闭的新文件")


'''
课堂小结：
1、return 要常用
2、拆包：吧列表/字典/元组  拆成多个值
列表/元组：*列表/元组    []()
字典：**字典 key=value   key=value   key=value

变量的作用域：
    没有讲函数的时候，没有讲作用域！！！
    有变量，封装在函数内部，仅函数可见！！！  ---局部变量。
    在py文件当中，在函数之外定义的变量  ---全局变量。整个py文件内部可以用
                                函数也可以使用，但是函数内部要修改全局变量时，要是有global
'''

'''
文件操作：打开，读、写追加、关闭
open函数：文件路径、打开模式（读写追加）、编码格式
读：read、readlines    --文件一定要存在
写：write（写、追加）--自己主动加\n换行。   文件可以不存在，会创建。但是还路金一定要存在
关闭：close

资源在使用之后，一定要释放，使用close()关闭释放
用法：with open() as fs:
        文件操作(read，write..)


'''
