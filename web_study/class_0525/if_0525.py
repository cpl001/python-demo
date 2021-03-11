"""
==================================
Author : "cpl"
Time : 23:20
Data : 2020/11/05
Project : web_study

===================================
"""
"""
if如果
if 条件1：
打印xxx
"""
score = input("考试成绩为:")
# if int(score) == 100:
#     print("优秀")

"""
if 条件1：
    条件1为真，那么打印该代码
else
    条件1不成立的时候，执行这条代码
"""
# if int(score) > 60:
#     print("优秀")
# else:
#     print("不及格")

"""
if 条件1：
    条件1为真，那么打印该代码
elif 条件2：
    条件2为真，执行该代码
elif 条件3：
    条件3为真，执行该代码
else
    都不成立的时候，执行这条代码
"""
if int(score) > 90:
    print("优秀")
elif int(score) > 70:
    print("良好")
elif int(score) > 60:
    print("及格")
else:
    print("不及格")

# 断点:你想再哪里让程序中断执行,由你自己来控制她的执行时间
# (觉得这个地方有问题会设置断点,1次不要设置太多断点 自己会懵逼)


# while
# while 条件1：
#     条件满足才会执行代码。
#   print("hello python")
#   一定要有一操作，使条件不成立




