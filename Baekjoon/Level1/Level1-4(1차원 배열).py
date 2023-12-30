'''


n=int(input())
arr=list(map(int,input().split()))

count=0
b=int(input())
for i in range(n):
    if(arr[i]==b):
        count=count+1
print(count)
---
a,b=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
count=0

for i in range(a):
    if(arr[i]<b):
        ans.append(arr[i])
        
print(*ans)

---

n=int(input())

arr=list(map(int,input().split()))
max=arr[0]
min=arr[0]

for i in range(n):
    if(max<arr[i]):
        max=arr[i]
    if(min>arr[i]):
        min=arr[i]
        
print(min,max)

---

arr=[]

for i in range(9):
    arr.append(int(input()))
    
max=arr[0]
num=0

for i in range(9):
    if(max<arr[i]):
        max=arr[i]
        num=i

print(max)
print(num+1)

---

n,m=map(int,input().split())
arr=[0 for i in range(n)]

for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a,b+1):
        arr[j-1]=c

print(*arr)

----
n,m=map(int,input().split())

arr=[]

for i in range(n):
    arr.append(i+1)
    
for i in range(m):
    a,b=map(int,input().split())
    tmp=arr[a-1]
    arr[a-1]=arr[b-1]
    arr[b-1]=tmp

print(*arr)
---


arr=[]

for i in range(30):
    arr.append(i+1)
    
for i in range(28):
    a=int(input())
    arr.remove(a)
    
print(*arr)

----

arr=[0 for i in range(10)]

count=0
flag=0
for i in range(10):
    a=int(input())
    arr[i]=(a%42)
    for j in range(i+1):
        if(j==i):
            continue
        if((a%42)==arr[j]):
            flag=1
            break
    if(flag==0):
        count=count+1
    else:
        flag=0
    
print(count)

---

import copy

n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(i+1)

arr2=copy.deepcopy(arr)

for i in range(m):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        arr[j-1]=arr2[b-j+a-1]
    arr2=copy.deepcopy(arr)

print(*arr)

---

n=int(input())

arr=list(map(int,input().split()))

max_score=max(arr)
max_index=arr.index(max(arr))
total=0

for i in range(n):
    total=total+arr[i]/max_score*100
    
total=total/n
print(total)

'''
