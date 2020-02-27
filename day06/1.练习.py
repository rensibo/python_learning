# while 嵌套
i = 1 #判断行数
while i <= 5: #一共有5行
    j = 1     #判断一行中有几个*号
    while j <= i:   #while嵌套
        print("* ",end="") #*后有一个空格间距，end=''是默认回车
        j += 1
    print("\n") #换行，注意对应的空格
    i += 1 #注意空格


# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d "%(j,i,j*i), end="")
        j +=1
    print("\n")
    i +=1
# %-2d是占位符，占两个位置，end=默认回车



## for 嵌套


## 找出1000以内的所有完数
for i in range(2,7):
    temp = 0
    for j in range(1,i):
        print(j)
        if i % j == 0:
            temp += j
            print(temp)
    if i == temp:
        print(i)

## 举例解析
#第一步：j从1--7之间进行取值，第一次取值为1；i从2--7之间进行取值，第一次取值为2
#          输出j为1
#          当:2%1==0时
#          temp=temp+1=0+1=1
#          输出j=1
#    第二步：j取值为2；i取值位2
#            输出j=2
#            当2%2==0
 #           temp=1+2=3
 #           输出j=2
  #  第三步：

   
   
   
    















'''for i in range(2, 1000):
    tmp = 0
    for j in range(1, i):
        if i % j == 0:
            tmp += j
    if i == tmp:
        print(i)'''