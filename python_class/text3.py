"""
控制流:代码的执行顺序 -- 从上之下依次执行 : 判断 循环
判断: if 语法
"""
# money = int(input("请输入你的余额: "))
# if money >= 500:
#     print("买别墅")
# elif money >= 200:
#     print("买一栋楼")
# elif money >= 50:
#     print("买奥迪Q5")
# else:
#     print("好好学习挣钱")

"""
成员运算符 in, not in
"""

# a = [1, 2, "6", "summer"]
# b = int([a])
# print(b)
# 判断元素是否在列表中
# exist = [1, 2, "6", "summer"]
# if "i" in exist:
#     print("i存在于列表中")
# else:
#     print("i不存在列表中")

#使用count()方法
# exist = [1, 2, "6", "summer"]
# if exist.count("i") == 1:
#     print("i 存在于列表中")
# else:
#     print("i 不存在于列表中")

# exist = [1, 2, "6", "summer"]
# zimu = "i"
# if zimu in exist:
#     print("{zimu} 存在于列表中")
# else:
#     print("{zimu} 不存在于列表中")

# exist = [1, 2, "6", "summer"]
# print("i" in exist)


#dict_1 = {"class_id":45,'num':20}，请判断班级上课人数是否大于5，注：num表示课堂人数

# dict_1 = {"class_id": 45, 'num': 20}
# num = dict_1.get("num")
# if dict_1['num'] >= 5:
#     print("班级人数为: {} ".format(num))
# else:
#     print('班级人数不足5人')



# list5 = []
# list1 = ["小咪咪","小狗狗","小土豆"]
# list2 = ["18","19","20"]
# list3 = ['Female','Man','Female']
# list4 = ["长沙", "武汉","南京"]
# for i in range(3):
#     dict1 = dict(name=list1[i],age=list2[i],sex=list3[i],city=list4[i])
#     list5.append(dict1)
# print(list5)