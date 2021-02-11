"""
1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
"""
# 方法1：
# price = int (input("请输入您的金额："))
# if 50 <= price <= 100:
#     discount = price * (1 - 0.1)
#     print('您要支付的金额为：{}'.format(discount)) #使用.format方法
# elif price >= 200:
#     discount = price * 0.2
#     print('您要支付的金额为：{}'.format(price - discount))
# else:
#     print('您需要支付的金额为：{}'.format(price))

# 方法2：
# money = int(input('请输入金额：'))
# if money in range(50,101):
#     # discount = 0.1
#     paymoney = money * (1 - 0.1)
#     print("您最终要支付的金额为：{}".format(paymoney))
# elif money >= 200:
#     paymoney = money * (1 - 0.2)
#     print("您最终要支付的金额为：{}".format(paymoney))
# else:
#     print("您最终要支付的金额为：{}".format(money))
"""运行结果：
请输入金额：2020
您最终要支付的金额为：1616.0"""


"""
2 判断是否为闰年
提示:
输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
什么是闰年，请自行了解（需求文档没有解释）
"""
# year = int(input('请输入年份：'))
# if year % 4 == 0 and year % 100 != 0:
#     print("{}是普通闰年".format(year))
# elif year % 400 == 0:
#     print("{}是世纪闰年".format(year))
# else:
#     print("{}不是闰年".format(year))
"""运行结果：
请输入年份：1999
1999不是闰年"""


"""
3.求三个整数中的最大值
提示：定义 3 个变量
"""
# num1 = int(input("请输入第1位数字："))
# num2 = int(input("请输入第2位数字："))
# num3 = int(input("请输入第3位数字："))
# if num1 > num2 and num1 > num3:
#     print('最大的数字是{}'.format(num1))
# elif num2 > num1 and num2 >  num3:
#     print('最大的数字是{}'.format(num2))
# else:
#     print(('最大的数字是{}'.format(num3)))
"""运行结果：
请输入第1位数字：32
请输入第2位数字：12
请输入第3位数字：23
最大的数字是32"""


"""
4，  使用for打印九九乘法表
提示：
输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
1 * 1 = 1
1 * 2 = 2  2 * 2 = 4	
1 * 3 = 3  2 * 3 = 6   3 * 3 = 9	
1 * 4 = 4  2 * 4 = 8   3 * 4 = 12  4 * 4 = 16	
1 * 5 = 5  2 * 5 = 10  3 * 5 = 15  4 * 5 = 20  5 * 5 = 25	
1 * 6 = 6  2 * 6 = 12  3 * 6 = 18  4 * 6 = 24  5 * 6 = 30  6 * 6 = 36	
1 * 7 = 7  2 * 7 = 14  3 * 7 = 21  4 * 7 = 28  5 * 7 = 35  6 * 7 = 42  7 * 7 = 49	
1 * 8 = 8  2 * 8 = 16  3 * 8 = 24  4 * 8 = 32  5 * 8 = 40  6 * 8 = 48  7 * 8 = 56  8 * 8 = 64	
1 * 9 = 9  2 * 9 = 18  3 * 9 = 27  4 * 9 = 36  5 * 9 = 45  6 * 9 = 54  7 * 9 = 63  8 * 9 = 72  9 * 9 = 81"""
for row in range(1,10):
     for col in range(1,row + 1):
         print('{} * {} = {}'.format(row,col,row * col),end='\t')#end用法，是将后面的显示在一行
     print()
"""运行结果：
1 * 1 = 1	
2 * 1 = 2	2 * 2 = 4	
3 * 1 = 3	3 * 2 = 6	3 * 3 = 9	
4 * 1 = 4	4 * 2 = 8	4 * 3 = 12	4 * 4 = 16	
5 * 1 = 5	5 * 2 = 10	5 * 3 = 15	5 * 4 = 20	5 * 5 = 25	
6 * 1 = 6	6 * 2 = 12	6 * 3 = 18	6 * 4 = 24	6 * 5 = 30	6 * 6 = 36	
7 * 1 = 7	7 * 2 = 14	7 * 3 = 21	7 * 4 = 28	7 * 5 = 35	7 * 6 = 42	7 * 7 = 49	
8 * 1 = 8	8 * 2 = 16	8 * 3 = 24	8 * 4 = 32	8 * 5 = 40	8 * 6 = 48	8 * 7 = 56	8 * 8 = 64	
9 * 1 = 9	9 * 2 = 18	9 * 3 = 27	9 * 4 = 36	9 * 5 = 45	9 * 6 = 54	9 * 7 = 63	9 * 8 = 72	9 * 9 = 81"""


"""进阶版
猜拳游戏"""
import random
player = int(input("请输入你要输入的拳数(1剪刀、2布、3石头):"))
computer = random.randint(1,3)
# print("您出{}".format(player))
# print("电脑出{}".format(computer))
if (player == 1 and computer == 2):
    print("您出剪刀，电脑出布.")
    print("真棒！小宝宝赢了哦~")
elif (player == 2 and computer == 3):
    print("您出布，电脑出石头.")
    print("真棒！小宝宝赢了哦~")
elif (player == 3 and computer == 1):
    print("您出石头，电脑出剪刀.")
    print("真棒！小宝宝赢了哦~")
elif player == computer:
    print('平局，再来！')
else:
    print("电脑赢啦~")
