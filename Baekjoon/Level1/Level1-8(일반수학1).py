Site : https://www.acmicpc.net/step/8
일반수학 1

'''
1. 진법 변환(2745)
진법에 대해 배우는 문제

import math

def becomenum(param):
    return (ord(param)-55)

n,b=input().split()
dec=0

b=int(b)
n=list(n)
n.reverse()

for i in range(len(n)):
    if(n[i].isalpha()):
        tmp=becomenum(n[i])
    else:
        tmp=int(n[i])

    dec=dec+tmp*math.pow(b,i)

print(int(dec))

---
2. 진법 변환2(11005)
반대 방향으로 진법을 변환하는 문제

import math

def becomenum(param):
    return (ord(param)-55)

def becomealpha(param):
    return (chr(param+55))
    
def findnum(param,param2):
    i=0
    while(1):
        if(math.pow(param2,i)>param):
           break
        i=i+1
    location = i-1
    num=int(param/math.pow(param2,location))
    return num,location


n,b=map(int,input().split())


i,j=findnum(n,b)
arr=[0 for i in range(j+1)]

while(1):
    if(n==0):
        break
    v1,v2=findnum(n,b)
    arr[(v2)]=v1
    n=n-v1*math.pow(b,v2)

for i in range(len(arr)):
    if(arr[i]>=10):
        arr[i]=becomealpha(arr[i])

arr.reverse()

if not arr:
    print(0)
else:
    print(*arr,sep="")


# 사람이 푸는 방식으로 푼 방식
# 제곱근 중 가장 큰 값을 계속해서 빼는 식으로 구함.

#a,b=map(int,input().split())
#
#print(a,b)
#
#while(1):
#    if(a==0):
#        break
#    print(int(a%b))
#    a=int(a/b)
#
# 이런 식으로 풀면 엄청 빨리 풀 수 있었음.. 나머지를 계속해서 구하는 방식






---
3. 세탁소 사장 동혁(2720)
💰
def cal(b,a):
    return int(a/b),(a-b*int(a/b))

def ref(param):
    a=b=c=d=0
    if(param>=25):
        a,param=cal(25,param)
    if(param>=10):
        b,param=cal(10,param)
    if(param>=5):
        c,param=cal(5,param)
    if(param>=1):
        d,param=cal(1,param)
    return a,b,c,d


n=int(input())

for i in range(n):
    a=int(input())
    print(*ref(a))

# 소수점으로 계산 진행 시, 오차발생
# 컴퓨터는 숫자를 2진수로 받아들이기 때문에 오류가 발생. -> 무한반복되는 근사값으로 값을 저장하기 때문에 오차발생
# 소수점으로 계산하고 싶으면 모듈 응용하면됨(decimal)

---
4.중앙 이동 알고리즘(2903)
둘씩 반복해서 나눴을 때 점의 개수를 세는 문제

import math
n=int(input())

a=int(math.pow(2,(n)))
print(int(math.pow(a+1,2)))

#한 변을 기준으로 갯수 카운트


---
5.벌집(2292)
벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제


---
6.분수찾기(1193)
분수의 순서에서 규칙을 찾는 문제


---
7.달팽이는 올라가고 싶다(2869)
달팽이의 움직임을 계산하는 문제


---

'''
