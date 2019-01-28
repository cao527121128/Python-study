#coding=utf-8
#队列：也是一种运算受限的线性表。它只允许在标的一端进行插入，而在另一端进行删除。队列亦称：先进先出FIFO表

import collections

#创建一个队列
queue = collections.deque()
print(queue)

#进队列--存数据
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)


#出队列--取数据
res1 = queue.popleft()
print("res1 =",res1)
print(queue)
res2 = queue.popleft()
print("res2 =",res2)
print(queue)
res3 = queue.popleft()
print("res3 =",res3)
print(queue)