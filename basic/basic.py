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