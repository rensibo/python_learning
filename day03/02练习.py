#输入年份，判断是不是闰年
year = int(input('请输入一个年份：'))
if year % 400 == 0:
    print('这是闰年')
else:
    print('这不是闰年')



year = int(input('请输入一个年份：'))
if year % 4 ==0 and year % 100 != 0:
    print('这是闰年')
else:
    print('这不是闰年')