"""
==================================
Author : "cpl"
Time : 22:20
Data : 2020/11/08
Project : web_study

===================================
"""

# 遍历：吧所有事情都经历一遍
# 主要针对的是列表和字典

# 定义一个列表
list_p = ["jnney", "jessic", "kitty", "tom", "carman"]
"""
for 变量 in 列表：
    得到每一个成员时，都会执行的代码

在这个列表当中，去取每一个车关于，赋值给变量。
变量 = 第一个成员
变量 = 第2个成员
变量 = 第3个成员
变量 = 第4个成员

通过列表的索引来遍历：
range：内置函数。
功能：生成整数序列。
起点：默认是0
终点：你给。
步长：默认为1
左闭右包：含起点
"""
# 遍历列表的值
# for item in list_p:
#     print(item)
#     if item == "kitty":
#         break
# 如果运行到kitty，就停止运行

# 遍历索引
"""
获取到列表的长度：6个
要遍历的索引：0，1，2，3，4，5

"""
# for index in [0,1,2,3,4,5]:
#     print(list_p[index])

# 默认从0开始，步长+1，终点：列表的长度
for index in range(len(list_p)):
    print(list_p[index])

# 字典遍历：从头取到尾
person_info = {"sex": "男", "tzh": "帅，有钱，会哄人", "age": 30}
# 键名还是值？
# 通过遍历键名。
for key in person_info.keys():
    print(key)
    print(person_info[key])
# 取字典遍历，这个方法用的不多，下面那个用的多
print("分隔一下~~~~")
# 遍历键值对（常用字典遍历方式）
for key, value in person_info.items():
    print(key, value)

"""
双重for循环
1、想清楚，外层是什么，内层干什么
有行又有列的这种
"""
"""
输出：
1
1 2
1 2 3
1 2 3 4
"""
# for index in range(1,5):
#     for sub in range(1,index+1):
#         print(sub,end=" ")
#     print("")#换行

for row in range(1, 5):
    for sub in range(1, row + 1):
        print(sub, end=" ")
    print("")

"""
总结：
1、for循环：
    列表
    字典

for item in 列表/字典.item():
        xxxx

2、range函数：生成整数序列，从0开始，步长为1

3、双重for循环   
1)可自己举案例找规律
2）梳理清楚：外层循环和内城循环的逻辑关系。
3)再编写双重for
4)根据输出内容，调整语句逻辑
"""






