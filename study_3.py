i = 1
while i <= 9: # 定义外层循环的控制变量
    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        print(f'{j} * {i} = {j*i}\t',end='') # 内层循环的语句,不要换行,通过 \t 制表符进行对齐
        j += 1
    i += 1
    print()
