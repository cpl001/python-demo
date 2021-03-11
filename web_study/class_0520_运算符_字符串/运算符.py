print("***********************运算符**************")
num1 = 10
num2 = 52
res = num1 + num2
print(res)

res = num2 - num1
print(res)

res = num1 * num2
print(res)

res = num1 / num2
print(res)

res2 = num1 % num2
print(res2)


print("***********************赋值运算**************")
"""
赋值运算：赋值给变量

巧克力120  小龙虾 88   红酒200
收银台结账   sum=0

"""
sum = 0
#sum = sum + 120
sum += 120
print(sum)

#小龙虾 80
sum += 80
print(sum)

#红酒 200
sum += 200
print(sum)

#在原来的基础上减掉红酒的钱
sum -= 200
print('最终支付的钱：',sum)

print("***********************比较运算符**************")
my_money = 200
you_money = 400

#==等于
print(my_money == you_money)
#!=不等于
print(my_money != you_money)
#大于>
print(my_money > you_money)
#大于等于
print(you_money >= my_money)
#小于
print(you_money < my_money)
#小于等于
print(my_money <= you_money)


print("***********************逻辑运算符**************")
#
# input函数
# age = input("请输出你择偶的年龄：")
# height = input("请输入你择偶的身高:")
# aslary = input("请输入你择偶的收入:")
#
# res3 = (int(age) > 25) and (int(height) >178) and (int(aslary) > 10000)
# print(res3)

# 语文写超过30个字 和 数学写20道题 和 背诵100个英文单词 才可以出去玩
# Chinese = input("语文写了：")
# math = input("数学写了：")
# english = input("英语背诵了：")
# res4 = int(Chinese) > 30 and int(math) > 20 or int(english) > 100
# print(res4)



