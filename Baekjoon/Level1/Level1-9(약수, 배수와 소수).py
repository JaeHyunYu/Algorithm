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


---
5.소수(2581)
2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 2


---
6.소인수분해(11653)
N을 소인수분해하는 문제
