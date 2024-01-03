Site : https://www.acmicpc.net/step/10
약수, 배수와 소수

'''
1.배수와 약수(5086)
배수와 약수를 배우는 문제

while(1):
    a,b=map(int,input().split())
    if(a==b==0):
        break
    if((b%a)==0):
        print("factor")
    if((a%b)==0):
        print("multiple")
    if(((b%a)!=0)&((a%b!=0))):
        print("neither")

---

2.약수 구하기(2501)
주어진 수의 약수를 구하는 문제
n,k=map(int,input().split())
count=0
i=0

while(1):
    if(count==k):
        break
    if(i==n):
        break
    i=i+1
    if(n%i==0):
        count=count+1

if(count==k):
    print(i)
else:
    print(0)

---

3.약수들의 합(9506)
약수를 구하면서 주어진 수가 완전수인지 판별하는 문제

while(1):
    n=int(input())
    if(n==(-1)):
        break
    total=0
    i=1
    arr=[]
    while(1):
        if(i==n):
            break
        if(n%i==0):
            total=total+i
            arr.append(i)
        i=i+1

    if(sum(arr)==n):
        print(n,"=",end=" ")
        for k in range(len(arr)):
            if(k==(len(arr)-1)):
                print(arr[k])
            else:
                print(arr[k],"+ ",end="")
    else:
        print(n,"is NOT perfect.")

---
4.소수 찾기(1978)
2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 1

n=int(input())
arr=map(int,input().split())
num=0
arr=list(arr)
for i in range(n):
    count=0
    for k in range(1,int(arr[i])+1):
        if(arr[i]%k==0):
            count=count+1
    if(count==2):
        num=num+1
print(num)


---
5.소수(2581)
2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 2

def prime(param):
    count=0
    for i in range(1,param+1):
        if(param%i==0):
            count=count+1
    if(count==2):
        return 1
    else:
        return 0

n=int(input())
m=int(input())

arr=[]

for i in range(n,m+1):
    if(prime(i)):
        arr.append(i)

if not arr:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])


---
6.소인수분해(11653)
N을 소인수분해하는 문제

n=int(input())
i=2
while(1):
    if(n==1):
        break
    if(n%i==0):
        n=int(n/i)
        print(i)
        continue
    else:
        i=i+1
        
