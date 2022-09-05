# for 循环

count = 0
name = 'itheima is a brand of itcast'
_1 = 0
for i in name: # 将name里面的内容挨个取出,赋予x临时变量
    if i == 'a':
        _1 += 1
print(f'在字符串\'{name}\'中一共有{_1}个a')

# range 语句

for x in range(10):
    print(x)

# 第二种
num1 = int(1)
num2 = int(5)

for x in range(num1,num2): # 表示从num1开始,到num2结束(不包含num2本身)
    print(x)
    
    
# 语法三
# range(num1,num2,step)

for x in range(1,10,2):
    print(x)
    # 意思是从数字1开始,数字10结束(不包含10本身) 步长为2 意思是每次加2
    # 输入结果应该是 1,3,5,7,9
    
    
    
    
# 作业
# 用range写法判断1-100个数字中有多少个偶数

count = 0
num = 200
noteven = 0

for i in range(1,num+1):
    if (i%2) == 0:
        count += 1
    else:
        noteven += 1
print(f'在{num}个数中,有{count}个偶数,有{noteven}个基数')



# 用 for循环向小美表白

bitch = '小美'
rose = 10 # 每天要送给小美的玫瑰花
day = 100 # 目标是表白一百天
i = 0

for i in range(1,int(day+1)):
    print(f"今天是第{i}天,深情的我继续向{bitch}表白")
    for c in range(1,int(rose+1)):
        print(f'送给{bitch}{c}朵玫瑰花')
    print(f'{bitch},我喜欢你')
    print()
print(f'直到第{i}天后,我向{bitch}表白成功了')

# 作业
# 用 for 循环打印99乘法表
_1 = 9
_2 = 9
for _1 in range(1,10):
    for _2 in range(1,_1+1):
       print(f'{_1} * {_2} = {_1*_2}\t',end="")
    print()
    


# continue 和 break


for i in range(1,6):
    print('语句一')
    continue
    print('语句二') # 下面这个语句二是不会执行的
    
    

# 演示continue的嵌套应用

for i in range(1,6): #2
    print('语句一')
    for v in range(1,8): #1
        print('语句二')
        continue
        print('语句三')
    print('语句四') 
    # continue 只会影响到循环1,所以语句三不执行,但是语句4会正常执行,因为语句四不在1那个循环内
    
    
# continue关键字用于: 中断所在循环的当次执行,直接进入下一次
# continue可以用于: for 循环和while循环,效果一致
   
   
# break

# break关键字用于: 直接结束循环
# break可以用于: for 循环和while循环,效果一致

# 注意 break 和 continue 在嵌套循环中,只能作用在所在的循环上,无法对上层循环起到作用

# 示例

for i in range(1,101):
    print('语句1')
    
    print('语句2')
    for g in range(1,500):
        print('语句3')
        break
        print('这样能过吗')

print('语句4')
# 最后结果肯定是只输出一次 语句1 和 语句4


# 练习案例 发工资

'''
某公司有 1w 元,给20名员工发工资

员工编号从1到20,从编号1开始,依次领取工资,每人可领取1000元

领工资时,财务判断员工的绩效分(1-10) (随机生成) 如果低于5,不发工资,换下一位

如果工资发完了,结束发工资
'''
company_money = 10000 # 公司资金
staff = 20 # 员工数量
salary = 1000 # 工资
Performance = 5 # 合格绩效分

import random # 导入随机数

for i in range(1,staff+1):
    performance = random.randint(1,10)
    
    if performance < Performance:
        print(f'员工{i},绩效分{performance},低于{Performance},不发工资')
        continue
    company_money -= salary
    if company_money < 0:
        print('公司没钱了,下个月再来领吧')
        break
    print(f'员工{i},发工资{salary}元,还剩{company_money}元')
    
if company_money > 0:
    print(f'工资发完了,还剩{company_money}元')
else:
    print(f'工资发完了,还欠{company_money}元')
    




    
 # 服了,居然要 嵌套式的循环
 
money = 10000
import random
for k in range(1,21):
    _1 = random.randint(1,10)
    if money <= 0 :
        print('抱歉,公司没钱了,下个月再来领工资吧')
        break
    if _1 < 5 :
        print(f'员工{k},绩效分{_1}分,低于5分,不发工资')
        continue
    if money >= 1000:
        money -= 1000
        print(f'员工{k},绩效分{_1}分,发工资1000,继续加油')
       

if money >= 0 :
    print(f'工资发完了,还剩{money}元')

    
# 最优雅的版本


# 函数
# len() 判断字符串的长度

def check_QR():
    print('欢迎来到黑马程序员\n请出示您的健康码和72小时核酸证明') # \n 和lua的换行符一样
check_QR()
