
"""
==================================
Author : "cpl"
Time : 22:20
Data : 2020/06/08
Project : web_study

===================================
"""

# 列表[list]  是一种数据类型。  字符串（str），布尔值（bool），整数（int），浮点数（float）
# 定义
list_my = [] #空列表  排队的队列里没人
print(list_my)

# 可以放任意类型的数据，可以重复
list_python30 = ["小米",20,"小红",True,"可爱多"]

# 有序的，通过下标取值，从0开始
# 取值方式：列表名[下标]
print(list_python30[2])#0下标取值是小米，1下标取值是20，2下标取值是小红，所以2的取值结果是小红
# 通过值获取它的下标 格式：列表名.index（数据）
print(list_python30.index(True))#下标为3

# 数据的不可变类型：数字，布尔值，字符串
# 列表：可变类型，可增删改

# 1.添加数据
# 1)追加在末尾，格式:列表.append(数据)
list_python30.append("深夜")
print(list_python30)#['小米', 20, '小红', True, '可爱多', '深夜']

# 2)插队: xiaoxiao，格式：列表.insert(索引,值) (了解即可）
list_python30.insert(-1,"xiaoxiao")
print(list_python30)#['小米', 20, '小红', True, '可爱多', 'xiaoxiao', '深夜']
list_python30.insert(0,"迷鱼")
print(list_python30)#['迷鱼', '小米', 20, '小红', True, '可爱多', 'xiaoxiao', '深夜']

# 3) 格式：列表1.extend(列表2): 将列表2追加到列表1   （了解）
new_list = ["小孩","豆豆",223]
list_python30.extend(new_list)
print(list_python30)


# 列表操作 - 修改数据
# 2.修改数据，找到索引，并修改索引对应的值
index = list_python30.index("可爱多")
list_python30[index] = "mingxing"#修改值
print(list_python30)
# ['迷鱼', '小米', 20, '小红', True, 'mingxing', 'xiaoxiao', '深夜', '小孩', '豆豆', 223]

# eg：
aa = list_python30.index("xiaoxiao")
list_python30[aa] = 22
print(list_python30)
# ['迷鱼', '小米', 20, '小红', True, 'mingxing', 22, '深夜', '小孩', '豆豆', 223]

# 下标越界
#找下标为18的值，但实际没有18，只有11，所以报错了
# print(list_python30[18])#IndexError: list index out of range

#3.删除数据
# 删除某一个位置的值
# 格式：列表.remove(数据)      删除列表当中第一次出现的指定数据
list_python30.remove("mingxing")
print(list_python30)

# del
# 格式：del 列表[]   删除列表下标中的数据
del list_python30[1]
print(list_python30)

# pop
# 格式：列表.pop()  删除列表末尾数据
list_python30.pop()
print(list_python30)

# clear
# 格式：列表.clear()  清空列表

# 获取列表的长度  len()
print(len(list_python30))

# 成员运算符
# 格式1： 成员 in 列表/字符串
# 格式2： 成员 not in 列表/字符串
result1 = "深夜" in list_python30
print(result1)#True

result2 = "sjj" in list_python30
print(result2)#False
result3 = "sjj" not in list_python30
print(result3)#True



