"""
==================================
Author : "cpl"
Time : 22:20
Data : 2020/06/08
Project : web_study

===================================
"""
"""
1、有以下数据来自于一个嵌套字典的列表（可自定义这个列表），格式如下：
person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,  .... 其他]
创建一个txt文本文件，来添加数据
a.第一行添加如下内容：name,age,gender,hobby,motto

b.从第二行开始，每行添加具体用户信息，例如：
yuze,17,男,假正经, I am yours cainiao,18,女,看书,Lemon is best!"""
# with open('homework0601.txt','a',encoding='utf-8') as fs:
#     fs.write("name,age,gender,hobby,motto")
person_info = [{"name":"yuze", "age": 18, "gender": "男",
"hobby": "假正经", "motto": "I am yours"} ,  .... 其他]
"""
一行一行的存储
字符串：yuze,17,男,假正经，I am yours
列表当中，每个字典的values.
list(字典.values())
用逗号将每一个values拼成一个字符串。
','.jion(列表/元组)---每一个成员要是字符串
再写入文件当中"""






"""
编写如下程序
有两行数据，存放在txt文件里面(手动建立文件，并添加如下数据)：
url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
[{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888',
'pwd':'123456'},{'url':'/futureloan/mvc/api/member/recharge',
'mobile':'18866668888','amount':'1000'}]
"""