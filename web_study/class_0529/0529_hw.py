"""
==================================
Author : "cpl"
Time : 22:20
Data : 2020/06/08
Project : web_study

===================================
"""
"""
1、定义函数：（要求：定义函数处理逻辑。input输入操作在函数之外。）
将用户输入的所有数字相乘之后对20取余数
用户输入的数字个数不确定"""

def sum_num(*args):
    sum = 1
    for item in args:
        sum *= item
    return sum % 20
a = sum_num(1,2,3,4)
print(a)








"""2、编写函数，检查传入列表的长度，如果大于2，
那么仅仅保留前两个长度的内容，并将新内容返回"""

# def getNum(num):
#     if len(num) > 2:
#         print(num[0:2])
#
# getNum([1,3,2,4])


"""3、列表去重定义一个函数 def remove_element(m_list):，
将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
"""
# m_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# def remove_element(m_list):
#     list1 = set(m_list)
#     print(list1)
#
# remove_element(m_list)







"""
4、编写如下程序（要求：定义函数处理逻辑。input输入操作在函数之外。）
尝试函数封装：
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
"""
# wegiht = int(input("输入体重："))
# hight = float(input("输入身高："))
# BMI = wegiht / hight ** 2
# print(BMI)
# def get_BMI(wegiht,hight):
#
#     if BMI <= 18.5:
#         print("低于18.5")
#     elif BMI >= 18.5 and BMI <= 25:
#         print("过轻18.5-25")
#     elif BMI >= 25 and BMI <= 28:
#         print("正常25-28")
#     elif BMI >= 28 and BMI <= 32:
#         print("过重28-32")
#     elif BMI >= 32:
#         print("肥胖")
#     else:
#         print("严重肥胖")
#
# get_BMI(wegiht,hight)



"""
5， 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
如果字符串不在字典中，则添加到字典中，并返回新的字典"""



"""6， 通过定义一个计算器函数，调用函数传递两个参数，然后提示选择
【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。"""
def Calculator(num1,num2,sum1):
    if sum1 == 1:
        return num1 + num2
    elif sum1 == 2:
        return num1 - num2
    elif sum1 == 3:
        return num1 * num2
    elif sum1 == 4:
        return num1 / num2
    else:
        print('运算符错误，重新输入：')

tt = 'N'
while tt == 'N':
    num1 = int(input("请输入第1个数字："))
    num2 = int(input("请输入第2个数字："))
    sum1 = int(input("请输入操作【1】加 【2】减【3】乘 【4】除"))
    uu = Calculator(num1,num2,sum1)
    print(uu)
    tt = input("是否退出程序(N/Y)")
    if tt == 'Y':
        print("退出程序")



"""
7， 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，
询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。(
（要求：定义函数处理逻辑。但是input输入操作在函数之外。在for循环当中，调用input和自己定义的函数)"""


def info(name,age):
    people = 0
    for num in range(0,10):
        name = input("请输入你的姓名")
        age = int(input("请输入你的年龄"))
        if age >= 15 and age<= 22:
            people = people + 1
            return people
res = info('name',21)
print(res)





