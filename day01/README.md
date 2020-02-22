## 标识符
    1.标识符中可以包含字母和数字和“_”（下划线），但是数据不可以作为标识符的开头
    2.在python中的标识符是区分大小写的
    3.以下划线开头的标识符是具有特殊意义的。以单下划线_foo的代表不能直接访问的类属性，需通过类提供的接口进行访问
      不能用from xxx import*而导入
    
## 保留字
    1.python中有32个保留字
    2.不能用保留字作为标识符
    
##判断类型
    1.常见的数据类型有整型int（），浮点型float（），复数complex()，字符串''等
    2.print(type(a))#判断a的数据类型并打印
    3.print(type(a) == foloat）#判断a的数据类型是不是浮点数并打印
    4.print(isinstance (a,int))#判断a的数据类型是不是整型并打印
       【isinstance() 函数来判断一个对象是否是一个已知的类型】
    5.布尔类型（boollean），只有true和false两个值通常来判断条件是否成立。如果变量值为0，则为false，否则为true
##数值运算符
    加   +
    减   —
    乘   *
    除   /
    幂   **  （例：a**b，a的b次方）
    返回除法的余数     %    （例：5/2=2.5，商2余1，取余数，最终得1）
    取商的整数部分     //   （例：5/2=2.5，取得数的整数部分，最终得2）
##while循环
     1.while后面要加判断词，或者判断次数；while true，则固定被看作永远为真的表达式；while （i<10）,循环的次数小于10次
     2.while循环语句中包括continue，和break两个标识符，continue表示跳过当次循环；break表示跳过当前循环
##for循环
     1.知道执行次数的时候一般用for，（执行一系列的元素，直至元素判断完）
     2.可以设置执行次数
##digit 
     1.digit 指0-9的任意一个数
     2.Return True if the string is a digit string, False otherwise
     3. isdigit() 方法检测字符串是否只由数字组成            
      