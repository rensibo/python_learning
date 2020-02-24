str = "abcdefghijklmn"
str2 = 'bbbb'

print(str[1])

# 注意点 ： 字符串范围取值时 [a:b] 这是一个左闭右开的取值范围
print(str[1:8]) # 输出bcdefgh

print(str[3:]) # defghijklmn

# 从右往左数 下角标计数从-1开始  这是一个左闭右开的取值范围
print(str[-3:]) # lmn
print(str[-4:-2]) # kl

print(str[:3]) #abc


str3 = str + str2
print(str3)

# 字符串的拼接 可以用+来处理 但是仅限于字符串之间
#print(3 + "a")
#print("a" + 3)

# * 重复输出字符串
print(str * 3)

print(str in str)
print("ac" not in str)

for key in str:
    print(key,end="\t")
print()

print("I am boy! age = %d, name = %s, high = %d" % (23,"小明",160))


# %d %s %f %e

print("this is a %e" % 2e-2)

# 从控制台输入两个字符串 判断他们的关系
one = input('请输入第一组数字：')
two = input('请输入第二组数字：')
if one in two:
    print('%s包含于%s' % (one,two))
else:
    print('one不包含于two,one = %s,two = %s' % (one,two))
if two in one:
    print('two包含于one,one = %s,two = %s' % (one,two))
else:
    print('two不包含于one,one = %s,two = %s' % (one,two))



line_one = float(input ('第一条边：'))
line_two = float(input ('第二条边：'))
line_three = float(input ('第三条边：'))
if line_one + line_two > line_three and line_one + line_three > line_two and line_three + line_two > line_one:#任意两边之和大于第三边
    p = (line_one + line_two + line_three)/2 #周长/2
    q = p * (p - line_one) * (p - line_two) * (p - line_three)
    s = q ** 0.512
    print ('三角形的面积是：%f' % (s)  )
else:
    print('你所输入的三边不能构成三角形')




index = 100
while  index < 1000:
    a = index // 100
    b = index // 10 % 10
    c = index  % 10
    if a**3 + b**3 + c**3 == index:
       print('this is a 水仙花数：%d ' % index)
    index += 1


