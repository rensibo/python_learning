## 面向对象编程介绍
    将数据和函数绑定在一起进行封装
    1、类和对象：类就是创建对象的模版，对象是真实存在的
    2、类的构成：
        类名
        类的属性：一系列数据（例如描述数据，颜色，身高，体重，等数据）
        类的方法：允许对类进行的操作方法（比如这个类可以做什么，也就是函数）
    3、定义类
        class Dog:   #定义一个🐶狗类，要用class开头，类名首字母要大写，如果是多个单词拼接，那么每个单词的首字母都需要大写
            def bark(self):   #定义一个函数（也就是类的方法），狗叫   （一定要加上self）
                print('汪汪汪'）        
            def run(self):    #定义狗可以跑
                print（'狗在跑'）
        xiaogou = Dog    #创建一只小狗
        xiaogou.bark()   #调用了狗叫的方法
        xiaogou.run()
        
        xiaogou.weight = 5   #添加小狗的属性，狗重5斤
        xiaogou.color = '黄颜色'   #添加属性颜色
        print(xiaogou.weight)
        print(xiaogou.color)