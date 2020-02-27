#判断3个整数的大小，并由小到大输出

a = 3
b = 2
c = 1
if a > b:
    t = a
    a = b
    b = t
if a > c:
    t = a
    a = c
    c = t
if b > c:
    t = b
    b = c
    c = t
print("%d %d %d" % (a, b, c))
