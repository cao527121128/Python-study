# coding=utf-8
import random
num = int(input("请输入您的号码："))
res = random.choice(range(100)) + 1
print("res =",res)
#判断是否中奖  num==res
if num == res:
    print("恭喜您中500万！")