# 没有严格缩进，在执行时会报错
if True:
    print('哈哈哈')
else:
    print('falsefalsefaksec')
# 多行语句
print('1' + \
	'2' + \
	'3')
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days[0])
# 变量赋值
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
print(counter)
print(miles)
print(name)

# Python有五个标准的数据类型：
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）
age = 100
print('my age:'+str(age))
del age #删除一些对象的引用
# print('my age:'+str(age)) #NameError: name 'age' is not defined

# 字符串
str1 = 'trytrytryshutdown'
# 使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起
print(str1[0:5])

# Python列表
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list)               # 输出完整列表
print(list[0])            # 输出列表的第一个元素
print(list[1:3])          # 输出第二个至第三个元素 
print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)       # 输出列表两次
print(list + tinylist)    # 打印组合的列表

# Python元组 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print(tuple)               # 输出完整元组
print(tuple[0])            # 输出元组的第一个元素
print(tuple[1:3])          # 输出第二个至第三个的元素 
print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)       # 输出元组两次
print(tuple + tinytuple)   # 打印组合的元组
# 如果二次同赋值，就会报错
# tuple[0] = 'modify value'  #TypeError: 'tuple' object does not support item assignment

# Python 字典 列表是有序的对象集合，字典是无序的对象集合。字典当中的元素是通过键来存取的，而不是通过偏移存取。
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict['one'])          # 输出键为'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

# // 取整除 - 返回商的整数部分（向下取整，即四舍五入之只舍不入）	
print(10//3)

# while循环
count = 0
while (count < 9):
	print('this count is:'+str(count))
	count = count + 1
print('Good bye!')
# 如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中，
# flag = 1
# while (flag): print('Given flag is really true!')