import keyword

print('hello')

a = 1 + \
    2 \
    + 3
print(a)

# zhushi


"""

"""

'''

'''

# 标识符
# 1. 2.
_abc = '123'
_abc = 456
print(_abc)

print(keyword.kwlist)

for key in keyword.kwlist:
    print(key)

maxlEngth = 1

#
a = 120.0
print(type(a) == float)

if a == 1:
    print("yes")
else:
    print("no")

print(isinstance(a, int))

if True:
    print(123)

bar = "True"
print(type(bar))

bar = bar == str(True)
print(bar)
print(type(bar))
# 布尔类型
# True False

# 复数 complex
foo = 4 + 2j
print(type(foo))

foo2 = 4 - 2j

result = foo * foo2
# 4^2 - （2j)^2 = 16 - 4j^2 = 16 + 4 = 20
print(result)

# Python 的基本数据类型 int float bool complex


## 数值运算符

# + - * / 加减乘除

# // 除法，然后取整，小数部分截断  %  **

print(5 / 2)
print(5 // 2)

print(5 % 2)  # 0.5  1  5 % 2 = 2 。。。 1

print(13 % 5)  # 3

# num = input("需要判断的数值：")

# 对输入的数值判断奇偶

#

while True:
    num = input("需要判断的数值：")

    # print(num.isdigit())

    # 123  abc

    # digit 0-9的任意一个数
    # Return True if the string is a digit string, False otherwise.
    if (num.isdigit() == 0):
        continue
    # try:
    #     num = int (num)
    # except ValueError:
    #     print("转化异常")
    #     continue
    # 判断奇数偶数
    if (int(num) % 2 == 0):
        print("这是个偶数" + str(num))
    else:
        print("这是个奇数" + str(num))
    break

# continue 和 break的区别
# 首先这连个关键字都是放在循环里面使用的
# continue 是跳过当次循环
# break 是跳过当前循环


num = "1234"

print(num.isdigit())

print(num.isdigit() == 1)

# print(~1)
