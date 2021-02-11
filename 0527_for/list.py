
"""
列表课操作索引，切片，加。乘，检查成员

"""
#列表各处格式
list1 = [12,'nihao',78,'hello','black','red','blue']
print(list1)

#访问列表里的值
# 索引 列表索引从 0 开始，第二个索引是 1，依此类推
print(list1[1])#nihao
print(list1[4])#black
# 索引也可以从尾部开始，最后一个元素的索引为 -1，往前一位为 -2，以此类推
print(list1[-1])#blue
print(list1[-7])#12
# 索引-截取
print(list1[0:3])#12, 'nihao', 78
print(list1[-2:])#'red', 'blue'

# 更新
list1[2] = 122
print(list1)#原来的78变成122

#删除
del list1[3]
print(list1)#原来的hello删除了

#列表脚本操作符
print(len(list1))#长度

# 组合
list2 = [4,56,33]
print(list1 + list2)#方法1

list2 +=[3,45,9]
print(list2)#方法2

# 重复
list3 =[4,56,33] * 2
print(list3)

# 判断元素是否再列表里面
# 3 in [1, 2, 3]

#嵌套
a = [1,2,3]
m = ["a",'b','c']
x = [a,m]
print(x)#[[1, 2, 3], ['a', 'b', 'c']]
print(x[1])# x里的['a', 'b', 'c']元素
print(x[1][2])#x里的['a', 'b', 'c']元素的c

#列表函数&方法
#函数
print(len(x))#len(list) x里面有2个元素
print(max(a))#max(list) a列表里最大的元素是3
print(min(m))#min(list) a列表里最小的元素是'a'
seq = (11,34,56)
print(list(seq))#list(seq) 将元组转换为列表

print("****************************************")
#方法
list5 = ['11','66',34,"11"]
#list.count(obj) 统计某个元素在列表中出现的次数
print(list5.count('11'))
#list.append(obj) 在列表末尾添加新的对象
list5.append(677)
print(list5)
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list6 = [1,34,21]
list6.extend(list5)#5 = ['11', '66', 34, '11', 677]
print(list6)#结果[1, 34, 21, '11', '66', 34, '11', 677]
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
print("list5中66的索引值：",list5.index("66"))#1
#list.insert(index, obj) 将对象插入列表
list5.insert(1,32)#在列表5索引为1的位置上插入32
print(list5)
# list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list5.pop()#['11', 32, '66', 34, '11', 677]-1
print(list5)#['11', 32, '66', 34, '11']
# list.remove(obj) 移除列表中某个值的第一个匹配项
list5.remove('11')#只能输入列表中第一个数据
print(list5)
# list.reverse() 反向列表中的元素
list.reverse(list5)
print(list5)
# list.sort( key=None, reverse=False) 对原表进行排序
list7 = ['d','w','a','c','y']
list7.sort(reverse = True)
print("排序：",list7)#['y', 'w', 'd', 'c', 'a']
# list.clear() 清空列表
list7.clear()
print('列表7：',list7)
# list.copy() 列表复制
list8 = [1,2]
list8 = list5.copy()
print('列表8：',list8)




