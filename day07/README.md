## 引用
    1、a = 100 ------->原先是指将100赋值给a，现意为在值为100的空间上粘贴一个标签a
    2、id(a)------>寻找a的位置在哪里
    3、当程序中空间所在的值修改时，该空间的位置不变
        num = [11,22,33,44]
        num2 = num
        num2[0] = 50------>将第0位数值修改为50
        num2 = [50,22,33,44]
        id(num2)------>返回的位置和刚开始num的位置是一致的，不改变
    4、可变类型：
        （1）列表 
        （2）字典 
       不可变类型：
        （1）数值类型 long、int，bool，float
        （2）字符串 str
        （3）元组 tuple
## 函数返回值
    1、想要有返回值一定要用到函数return，如果一段程序中含有多个return，程序只会执行一个并不会执行其他
       也就是说return一旦调用，则立即结束当前函数，类似break，但break是结束整体代码块
    2、 想要使用return返回多个值的时候，可以选择将函数名用多个"，"逗号隔开进行返回
        return name,myId,age ----->这样返回的是三个值
        也可以使用元组类型，列表类型，以及字典类型
        return(name,myId,age)
        return[name,myId,age]   
        return{"name":name,"id":myId,"age":age}----->函数名不需要加""双引号
    3、最简单的方式推荐直接返回函数名，但是直接返回函数名、以元组或者列表返回时，是不考虑耦合关系的，必须按照一定的顺序进行返回，如果顺序出错，那么返回值存在不对称或者错误
       但是用字典的方式则是相当于对函数进行的一层封装，不会出现顺序错误
## 程序的思路及整体框架
    正向推导
    反向思考
## 缺省参数
    可以理解为默认的参数，不用赋值直接默认为一个数，即可不用传参
    1、参数中有缺省参数，一定要放在最后面
    2、可存在多个缺省参数
## 不定长参数
    1、参数的长度可变，可以传多个值
        def test(a,*b)------>*b代表的就是不定长参数b
            result = 0
            result += a
            for X in b------->遍历参数b
                result += X
            return result----->这里得出的结果是a+b（b代表的是所有b中的值相加）
        addResult = addAll(1,2,3,4,5)-----这里1会赋值给a，剩下的数2，3，4，5将会赋值给b
        print(addResult)----->这里值为1+2+3+4+5所得到的值
    2、返回值是字典的表示
        def test2(a,*b,**c)------>这里的a为必传值，**c则为字典
            print(a)---->返回值为1
            print(b)---->返回值为（2,3,4)
            print(c)---->返回值为{"m":5,"n":6}
        test2(1,2,3,4,m=5,n=6)
        
## 备注
    1、赋值运算符在使用时，例如a+=a其实是对a这个数据直接进行了修改，打印出来的结果将会是a+a之后的结果
       但是a=a+a其实是现在给a进行了一个定义，然后进行了修改，在打印是a的结果是原来a的值