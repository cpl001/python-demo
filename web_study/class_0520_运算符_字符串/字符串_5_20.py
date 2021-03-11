print("***********************字符串**************")
# 字符串成双成对，双引号开头，结尾也必须是双引号结尾。单引号开头，结尾也必须以单引号结尾。
print("nihao,好好学习哦！")
print('你今天美美哒')

# 字符串操作
person_info = '今是天6月1号，儿童节，要好好学习天天做作业哦！！'
# 取某一个位置的值
# 从0开始，正向  1，逆向  -1   变量名[索引]
print(person_info[3])
print(person_info[12])
print(person_info[-3])

# 区间取值   子字符串    有起点--结束点  步长
# 从0开始，到下标为6    变量名[起:结束]
print(person_info[0:4])     #取0，1，2，3，位置的内容，取左不取右：今天是6
print(person_info[:14])     #取0-14的内容：今天是6月1号，儿童节，要好
print(person_info[2:])      #取2-最后的一位的内容
#如果步长为正数，表示正向切片。如果步长为负数，则是逆向切片
print(person_info[:9:2])    #取0-9位的数字，步长位2：今是月号儿  //步长2，正向取值
print(person_info[4::-2])   #从第四位逆向取值，步长为-2，逆向取值：月天今
print(person_info[::-1])    #！！哦业作做天天习学好好要，节童儿，号1月6天是今
print(person_info[-1:-10:-1]) #！！哦业作做天天习

print("*************字符串常用操作方法/功能***********")
# 查找子字符串，找到返回的值都是>=0，没找到返回的就是-1
# find查找
index = person_info.find("今是天6月")
print(index)

a = "你今天真可爱，但是你更漂亮,very"
index = a.find("漂亮")
print(index)

# count计数
index = a.count("你")
print(index)

# len长度
print(len(person_info))
print(len(a))

#upper() 将字符串的字母转换成大写，重新生成一个字符串，不会修改原来的字符串
res = a.upper()
print(res)

# lower 小写
res = a.lower()
print(res)




