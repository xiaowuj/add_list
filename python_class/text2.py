
'''
#常用数据类型:列表[数组]、元组(小括号)、字典{}、激活
1、元素可以是任意的数据类型:int float bool str list tuple...
2、取值: 索引去取值--类比字符串
3、列表的元素是可以改变的 --增删改
4、列表元素可以重复的 -- 统计个数
5、tuple元组()--素可以是任意的数据类型--不能被改变--可以统计个数
'''

#list1 = [20, 20,20,3.14, 1314, "小吴", [1,2,3,4,5]]
#print(list1[4][1])     #嵌套取值
#print(list1[2:4])      #切片
#list1.append("骚鸡")    #新增 默认添加到尾部
#list1.insert(4,"小花")  #插入 ("目标位置","插入的内容")
#list1.extend(["双十一","双十二","小丑"]) #批量添加合并
#list1.pop(0)             #默认删除最后一个元素
#list1.remove(1314)       #指定元素本身删除
#list1.clear()            #清除所有元素
#list1[3]= "小红"          #修改
#list1.append("小吴")      #重新赋值
#print(list1.count("小吴")) #统计个数的长度
#print(len(list1))          #查看数组长度


tuple1 = (20, 20,20,3.14, 1314, "小吴", [1,2,3,4,5]) #元组
#list1[-1] = "小王八" #不能被修改
print(tuple1.count(20)) #查看统计个数
#如果非要改变 先把元组转换成列表 再修改
list1 = list(tuple1)
list1[-1] = "小丑"
list2 = tuple(list1)
print(list2)

# t = (20, 20,20,3.14, 1314, "小吴", [1,2,3,4,5])
# t_slice = t[6][1]
# print(t_slice)

#字典: dict {}
#1、元素: key:value(键值对)
#2、场景: 存储数据属性 : 人--名字 身高 体重
# key:不能是改变的数据类型(list,dict)---字符串，不能重 复唯一的
# value:可以是任何数据类型
#3、字典是没有顺序的--不能用索引去取值 取值通过key去取value
#dict1 = {"name":"小吴","height":"175","weight":"110"}
# print(dict1["name"])          #取值
# print(dict1.get("name"))      #取值
# dict1["height"] = "180"       #修改
# dict1["age"] = 18             #key不存在 新增加键值对最后
# dict1.pop("name")             #指定key删除 对应的键值对
# #del dict1
# # #del 删除所有，打印出来未定义
# dict1.update({"ciyt" : "武汉"}) #拼接合并
# print(dict1)
"""
集合:set {}, 元素单个
1、无序
2、元素不可以重复 -- 使用场景:去重
"""
# list2 = [11,22,33,11,22,33,11]
# set1 = set(list2)          #去重 set()函数转换成集合
# print(set1)
# list3 = list(set1)         #转换成数字列表
# print(list3)
"""
面试官问有用过集合吗？
回答: 做个东西在项目中用得很少，
但是我知道他是一个无序的而且元素是不可以重复的数据类型
"""





