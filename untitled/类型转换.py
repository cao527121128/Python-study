#coding=utf-8

#list--> set
l1 = [1,2,3,4,4,3,2,1]
s1 = set(l1)
print(s1)

#tuple --> set
t2 = (1,2,3,3,2,1)
s2 = set(t2)
print(s2)

#set --> list
s3 = {1,2,3,4}
l3 = list(s3)
print(l3)


#set --> tuple
s4 = {1,2,3,4}
t4 = tuple(s4)
print(t4)