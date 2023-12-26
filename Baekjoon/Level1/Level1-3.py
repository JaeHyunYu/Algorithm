'''
a=int(input())
for i in range(1,10):
   print(a,"*",i,"=",a*i)

----
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    print(b+c)
---
n=int(input())
total=0
for i in range(1,(n+1)):
    total=total+i
print(total)

---

total=int(input())
sum=0
n=int(input())

for i in range(n):
    a,b=map(int,input().split())
    sum=sum+a*b

if(total==sum):
    print("Yes")
else:
    print("No")
---

a=int(input())
a=int(a/4)
print("long "*a,"int",sep="")

---

import sys

n=int(sys.stdin.readline())

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)
'''
