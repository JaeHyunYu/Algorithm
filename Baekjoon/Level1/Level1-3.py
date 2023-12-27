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
    
---
a=int(input())
for i in range(1,(a+1)):
	b,c=map(int,input().split())
	print("Case #",i,": ",b+c,sep="")
---
a=int(input())
for i in range(1,(a+1)):
	b,c=map(int,input().split())
	print("Case #",i,": ",b," + ",c," = ",b+c,sep="")
---
a=int(input())
for i in range(1,(a+1)):
    print("*"*i)
---
a=int(input())
for i in range(1,(a+1)):
    print(" "*(a-i),"*"*i,sep="")
---
while(1):
    a,b=map(int,input().split())
    if(a==b==0):
        break
    print(a+b)

---
while(1):
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break

#EOF문제
'''
