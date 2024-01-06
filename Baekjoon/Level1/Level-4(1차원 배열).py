Site: https://www.acmicpc.net/step/6
1차원 배열

'''
1. 개수 세기(10807)
배열을 입력받고 v를 찾는 문제

n=int(input())
arr=list(map(int,input().split()))

count=0
b=int(input())
for i in range(n):
    if(arr[i]==b):
        count=count+1
print(count)
---
2. X보다 작은 수(10871)
배열을 입력받고 X보다 작은 수를 찾는 문제

a,b=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
count=0

for i in range(a):
    if(arr[i]<b):
        ans.append(arr[i])
        
print(*ans)

---
3.최소, 최대(10818)
최솟값과 최댓값을 찾는 문제

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
4. 	최댓값(2562)
최댓값이 어디에 있는지 찾는 문제

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
5. 공 넣기(10810)
배열에 값을 쓰는 문제

n,m=map(int,input().split())
arr=[0 for i in range(n)]

for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a,b+1):
        arr[j-1]=c

print(*arr)

----
6. 공 바꾸기(10813)
배열의 값을 교환하는 문제

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
7. 과제 안 내신 분..?(5597)
과제 제출 기한이 지났습니다.

arr=[]

for i in range(30):
    arr.append(i+1)
    
for i in range(28):
    a=int(input())
    arr.remove(a)
    
print(*arr)

----
8. 나머지(3052) 
배열을 활용하여 서로 다른 값의 개수를 찾는 문제

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
9. 바구니 뒤집기(10811)
배열을 뒤집는 문제

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
10. 평균(1546)
평균을 조작하는 문제

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
