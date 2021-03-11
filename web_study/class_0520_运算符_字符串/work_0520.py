"""
==================================
Author : "cpl"
Time : 22:20
Data : 2020/06/08
Project : web_study

===================================
"""

# 1、现在有字符串：str1 = 'python cainiao 666'
#     1、请找出第 5 个字符。
str1 = 'python cainiao 666'
print(str1[5])

#     2、请复制一份字符串，保存为 str_two(使用赋值哦)
str_two = str1
print(str_two)

#     3、请找出最中间的字符。（字符串长度是偶数。）
print(str1[9:11])

# 2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，
# 最后计算出应该支付的金额！（不需要校验数据，都传入数字就可以了。）
#       (使用input方法获取用户输入哦)

# print('请输入橘子的价格：')
# price = float(input('请输入橘子的价格：'))
# wegiht = float(input('请输入橘子的重量：'))
# sum = price * wegiht
# print(sum)

# 3.演练字符串操作
my_hobby = "Never stop learning!"
# 截取从 位置2 ~ 位置6 的字符串
print(my_hobby[2:6])
# 截取从 位置2 ~ 末尾 的字符串
print(my_hobby[2:])
# 截取从 开始位置~ 位置6 的字符串
print(my_hobby[:6])
# 截取完整的字符串
print(my_hobby[:])
# 从 索引3 开始，每2个字符中取一个字符
print(my_hobby[3::2])
# 截取字符串末尾两个字符
print(my_hobby[-1:-3:-1])
# 字符串的倒序
print(my_hobby[::-1])
# 说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），“索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）
