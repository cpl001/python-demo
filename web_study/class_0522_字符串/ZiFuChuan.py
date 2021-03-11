# """
# ==================================
# Author : "cpl"
# Time : 22:44
# Data : 2020/06/10
# Project : web_study
#
# ===================================
# """
#
# print("***********************字符串**************")
# # 字符串成双成对，双引号开头，结尾也必须是双引号结尾。单引号开头，结尾也必须以单引号结尾。
# print("nihao,好好学习哦！")
# print('你今天美美哒')
#
# # 字符串操作
# person_info = '今是天6月1号，儿童节，要好好学习天天做作业哦！！'
# # 取某一个位置的值
# # 从0开始，正向  1，逆向  -1   变量名[索引]
# print(person_info[3])
# print(person_info[12])
# print(person_info[-3])
#
# # 区间取值   子字符串    有起点--结束点  步长
# # 从0开始，到下标为6    变量名[起:结束]
# print(person_info[0:4])     #取0，1，2，3，位置的内容，取左不取右：今天是6
# print(person_info[:14])     #取0-14的内容：今天是6月1号，儿童节，要好
# print(person_info[2:])      #取2-最后的一位的内容
# #如果步长为正数，表示正向切片。如果步长为负数，则是逆向切片
# print(person_info[:9:2])    #取0-9位的数字，步长位2：今是月号儿  //步长2，正向取值
# print(person_info[4::-2])   #从第四位逆向取值，步长为-2，逆向取值：月天今
# print(person_info[::-1])    #！！哦业作做天天习学好好要，节童儿，号1月6天是今
# print(person_info[-1:-10:-1]) #！！哦业作做天天习
#
# print("*************字符串常用操作方法/功能***********")
# # 查找子字符串，找到返回的值都是>=0，没找到返回的就是-1
# # find查找
# index = person_info.find("今是天6月")
# print(index)
#
# a = "你今天真可爱，但是你更漂亮,very"
# index = a.find("漂亮")
# print(index)
#
# # count计数
# index = a.count("你")
# print(index)
#
# # len长度
# print(len(person_info))
# print(len(a))
#
# #upper() 将字符串的字母转换成大写，重新生成一个字符串，不会修改原来的字符串
# res = a.upper()
# print(res)
#
# # lower 小写
# res = a.lower()
# print(res)
#
# split() 分割。  分隔符：
# sep：分隔符
#maxsplit:1  分割的次数

person_info1 = "我是柠檬班30期的学生，我叫深夜吃糖，要天天不学习 yeah!"
print(person_info1)

str1 = person_info1.split("，")
print(str1)#['我是柠檬班30期的学生', '我叫深夜吃糖', '要天天不学习 yeah!']

str_pian = person_info1.split("，",1)
print(str_pian)#['我是柠檬班30期的学生', '我叫深夜吃糖，要天天不学习 yeah!']
str_pian = person_info1.split("，",2)
print(str_pian)#['我是柠檬班30期的学生', '我叫深夜吃糖', '要天天不学习 yeah!']
str_pian = person_info1.split("，",3)
print(str_pian)#['我是柠檬班30期的学生', '我叫深夜吃糖', '要天天不学习 yeah!']

# join()  拼接  按照分隔符将其拼接起来
# 将支离破碎的几个字符，拼接成一个完整的字符串！
# 1.拼接符:字符串：；
ss = ";".join(str_pian)
print(ss)#我是柠檬班30期的学生;我叫深夜吃糖;要天天不学习 yeah!
s2 = "  ".join(str_pian)
print(s2)#我是柠檬班30期的学生  我叫深夜吃糖  要天天不学习 yeah!

# replace  替代操作
# 原字符串要被替换成新的字符
sss = person_info1.replace("我","你")
print(sss)#你是柠檬班30期的学生，你叫深夜吃糖，要天天不学习 yeah!
s3 = sss.replace("你","小明")
print(s3)#小明是柠檬班30期的学生，小明叫深夜吃糖，要天天不学习 yeah!

# 格式化 format函数
# 格式：字符串名.format
# 动态的去改变字符串的值：占位符{}，有几个占位符，就需要几个替换参数
# age = input("年龄:")
# name = input("姓名:")
# 1.
# print("我的姓名是{}，我的年龄是{}岁".format(name,age))

# 2。有一些数据需要重复使用，在占位符{}里加索引
# print("我的姓名是：{0},我的年龄是：{1}岁，我的老师是：{0}".format(name,age,name))

# 字符串拼接 :
# 转义字符： \n 换行
print("hello,world! \n 你好世界！")
# \t 空tab（一个tab的长度）
print("hello,world! \t 你好世界！")
#r  取消转义,正常输出
print(r"hello,world! \t 你好世界！")
# + 字符串
str3 = "helloworld"
str4 = "hello python30"
str5 = "goodboy"
print(str3 + "\t" + str4 + "\t" + str5)

