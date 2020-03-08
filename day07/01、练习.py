# encoding: utf-8
# 统计人名姓氏个数，
# 张 三，
# 李 四，
# 王 武，
# 诸葛 四郎，
# 欧阳 克，
# 张 六

# 首先
resultNameCount = {}  #定义变量resultNameCoun是一个字典类型
fileName = "names.txt"  #定义变量fileName 是格式为txt的name文件
file = open(fileName)    #定义一个file打开fileName中的name.txt文件

line = file.readline()   #定义line为文件file中阅读行，逐行读取

while line:
    surname = line.split(" ")[0]  #定义surname为由空格分割开的下角标为0的值（姓和名由空格键隔开，姓的位置是0）
    currentCount = resultNameCount.get(surname)   #定义currentCount是取出来的姓氏的计数值
    if currentCount is None:    #判断获取的姓氏计数值是否为0
        resultNameCount[surname] = 1   #为0，则将字典中取出的姓氏赋值为1
    else:
        currentCount += 1  ##如果存在，则将字典中的该姓氏后的值+1 value值为2
        resultNameCount[surname] = currentCount   #再将计数值currentCount与resultNameCount[surname]对应起来

    line = file.readline() #阅读下一行

# 输出结果
for item in resultNameCount:  ##遍历整个只有保存了姓氏的字典
    print("姓氏：%s 出现的个数：%d" % (item, resultNameCount[item]))  #按照姓氏：个数的姓氏输出
