#coding=utf-8
#栈：是限制在表的一端进行插入和删除运算的线性表。栈又称后进先出简称：LIFO表

#示例1
#模拟栈结构
stack = []

#压栈--向栈里存放数据 A B C
stack.append("A")
print(stack)
stack.append("B")
print(stack)
stack.append("C")
print(stack)

#出栈--向栈里取出数据
res1 = stack.pop()
print("res1 = %s" % (res1))
print(stack)

res2 = stack.pop()
print("res2 = %s" % (res2))
print(stack)

res3 = stack.pop()
print("res3 = %s" % (res3))
print(stack)

