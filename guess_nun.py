import random
_1 = random.randint(1,10) # 获取1到100的随机数字

_2 = int(input('请猜猜数字(一直猜)'))
_3 = 1
global true,false

true = True
false = False

while true:
    if _1 == _2:
        print('猜对了')
        print(f'总共猜了{_3}次') # 猜对了将记录_3的值
        true = false # 将true改为false,让循环条件停止
    else:
        _3 += 1 # 每猜错一次,_3就会累计加一
        if _1 > _2:
            print('数字猜小了')
            _2 = int(input('请猜猜数字(一直猜)'))
        else:
            print('数字猜大了')
            _2 = int(input('请猜猜数字(一直猜)'))
