"""
for循环: 遍历 数据对象你面的所有元素: str,list,tuple dict
for 变量名 in 数据对象
    子代码(循环体)
循环多少次由什么决定的? -- 元素的个数
中断: break 跳出整个循环
跳出本次循环: continue

range() -- 内置函数: 生成一个整数序列,1,2,3,4,5,6
跟 for 循环一起使用:start-开始，stor-结束，step-步长  跟切片一样取头不取尾
"""
# cuunt = 0   # 计数器
# list1 = ['霸王别姬','小哥','小丑','双十二','吴邪']
# for name in list1:
#     if name == "小丑":
#        # break
#        continue
#     print(name)
#     print("*"*20)
#     cuunt +=1
# print(cuunt)
# print(len(list1))

# for i in range(1, 5):
#     print(i)


"""
函数: 封装成函数，调用。 === 提高代码的复用率，提高执行的效率
语法:
def 函数名():
    子代码(函数体)--实现功能
def() 函数调用

1、必备参数按位置传: 定义了就必须要传入的参数--不传就会报错
2、关键字传: 可以定义的时候赋值一个默认值
3、混合传: *args 不定长参数: 接受不确定的参数 -- 可以不传，可以传多个 == 接受元组
   **kwargs: 
"""


# def good__gob(salary, bouns, subsidy=500, *args, **kwargs):
#     sum1 = salary + bouns + subsidy
#     for i in args:
#         sum1 += + i
#     for j in kwargs:
#         sum1 += kwargs.get(j)
#     return sum1, salary
# result = good__gob( 4000, 800, 1000, 2000,aa=50,bb=60,cc=70)
# if result >= 8000:
#     print("这工作还可以")
# else:
#     print("这工作不满足我")

# print(result,)

"""
有进有出: 进 -- 参数,出 -- 返回值
返回值: 函数可以给到外面的数据调用 return获取返回值
"""

"""
1、完成任意整数序列的相加--range()— 生成一个整数序列,里面全是数字，求里面所有数字的和
2、定义函数:判断一个对象(列表,字典,字符串)的长度是否大于5,如果大于5,输出True,否则输出False
"""
# def add_fun(num):
#     sum = 0
#     for i in range(num):
#         sum += i
#     print(sum)
# add_fun(100)

def function_len(object):
    if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):
        leng = len(object)
        if leng >= 5:
            print("True")
        else:
            print("False")
    else:
        print("数据类型不能计算长度!")

function_len({1,2,3,4,5})










