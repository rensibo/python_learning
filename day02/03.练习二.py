index = 100
while index < 1000:
    a = index % 10  # 个位
    b = index // 10 % 10  # 十位
    c = index // 100  # 百位
    if a ** 3 + b ** 3 + c ** 3 == index:
        print("这是一个水仙花数：%d" % index)
    index += 1


