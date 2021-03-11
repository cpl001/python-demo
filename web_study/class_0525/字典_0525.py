"""
==================================
Author : "cpl"
Time : 22:20
Data : 2020/06/08
Project : web_study

===================================
"""
# 列表的排序，反转（面试可能问到）
# 按照从小到大 - 降序、升序
num_list = [100,234,22,445,54,98,90,34,389]
num_list.sort()#升序 - 从小到大
print(num_list)#[22, 34, 54, 90, 98, 100, 234, 389, 445]
num_list.sort(reverse=True)#降序 - 从大到小
print(num_list)#[445, 389, 234, 100, 98, 90, 54, 34, 22]
num_list.sort(reverse=False)
print(num_list)

#反转
print(num_list[::-1])#反转 [445, 389, 234, 100, 98, 90, 54, 34, 22]
print(num_list)#不反转  [22, 34, 54, 90, 98, 100, 234, 389, 445]

num_list.reverse()#修改原列表 [22, 34, 54, 90, 98, 100, 234, 389, 445]
print(num_list) #[445, 389, 234, 100, 98, 90, 54, 34, 22]



print("******元组*******")
# ()括号 - tuple元组
# 可以是任意类型。
# 如果以后准备的数据高过1个，不会对他做修改，可以使用元组，元组数据可以重复
my_tuple = ()#有序，以，分割成员
my_tuple2 = (18,22,43,3,98,22,699)
print(my_tuple2[2])

my_tuple3 = ("nhao")
print(type(my_tuple3))#<class 'str'> 元组3的类型是字符串的原因是没有加入一个元组的分割符","
my_tuple3 = ("nhh ",)
print(type(my_tuple3))#<class 'tuple'>



print("******字典*******")
# 字典 dict dictionary
# ()   无序    key唯一
dog_info = {
    "name":"钱罐",
    "sex":"公",
    "age":"3个月",
    "type":"串串",
    "owner":"陈多多"
}
my_dict = {}    #空字典
print(dog_info)

print(dog_info["name"])#钱罐  取值用中括号
# 取不存在的值会报错
# print(dog_info["parent"])# 报错：KeyError: 'parent'
print(dog_info.get("name")) #格式:字典.get(键名)
print(dog_info.get("parent"))#None  这么取值不会报错

# 添加 修改键值对
# 如果键名不存在字典当中，那就是添加键值对
# 如果键名存在与字典当中，那就是修改键值对应的值
# 添加键值对不可以选择位置添加，他是无序的
dog_info["age"] = "2个月半"#修改
print(dog_info)
dog_info["father"] = "金毛"#添加
print(dog_info)

#添加字典2到字典1  格式：字典1，update(字典2)
dog_other_info = {"color":"香槟色","size":"50cm"}
dog_info.update(dog_other_info)
print(dog_info)

# 字典里面，可以成员是字典吗？可以成员是列表吗？
# 字典加入字典
dog_info["other_info"] = dog_other_info
print(dog_info)
# 字典加入列表
dog_list = ["金毛",22,"公"]
dog_info["ddog_list"] = dog_list
print(dog_info)

# 删除del 格式：del 字典[key]
# del dog_info["father"]
# print(dog_info)
# pop 格式：字典.pop(key)    将列表2的数据追回到列表中
dog_info.pop("father")
print(dog_info)




