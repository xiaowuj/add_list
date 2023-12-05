# import keyword
# print(keyword.kwlist)
'''
关键字['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
# 匿名要起到见名知意
# print() 内置函数，打印输出到控制台(console)
# Python常用数据类型 整数(int) 浮点数(float) 布尔类型(bool)

'''
检测数据类型:
1)type() 判断数据类型
2)isinstance() 判断你给定的内型是否跟里面一样的，结果是bool值
字符串(str) 被成对引号包裹的内容字符串 有3种字符串
1)双引号和单引号一般结合嵌套关系
2)三引号可以保持格式，所见即所得
字符串取多个值———切片——[开始:结束:步长] 去头不去尾
replace()替换字符串里面的元素
'''
# info = "小吴最帅气"
# name = "小文最骚气"
# str1 = "hello world!"
# str1 = str1.replace("hello","da")
# # print(str1[0:7:5])
# print(str1)

# num = input("请输入姓名: ")
# num1 = input("请输入年龄: ")
# num2 = input("请输入性别: ")
# print("*****************")
# print("姓名：" + num)
# print("年龄: " + num1)
# print("性别: " + num2)
# print("*****************")

# num = input("请输入姓名: ")
# num1 = input("请输入年龄: ")
# num2 = input("请输入性别: ")
# print("*****************")
# print("""姓名: {}
# 年龄: {}
# 性别: {}""".format(num,num1,num2))
# print("*****************")

str1 = 'pythun hello aaa 123123aabb'
print(str1[0:6:1])
print('o a' in str1)
print('he' in str1)
print('ab' in str1)
str2 = str1.replace('pythun','lemon')
print(str2)
print(str2.index("aaa"))
print(str2.find("aaa"))
# '0 a' 'he' 'ab'
