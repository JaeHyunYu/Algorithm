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

n=int(input())

total=1
i=1
while(1):
    if(n<=total):
        print(i)
        break
    total=total+i*6
    i=i+1

# 한바퀴가 증가할 수록 6의 배수 형식으로 갯수가 늘어남(규칙성)

---
6.분수찾기(1193)
분수의 순서에서 규칙을 찾는 문제

import math
def findnum(param):
    i=1
    total=0
    while(1):
        for k in range(1,i+1):
           total=total+k
        if(param<=total):
            break
        i=i+1
        total=0
    return i,total-i+1
        
n=int(input())

a,b=findnum(n)
# a=가로로 몇번째에있는지, b=그 숫자가 무엇인지

distance=n-b+1
#distance = 그 라인에서 몇번째에 위치하고 있는지(1부터 시작)

mid=math.ceil(a/2)
# 그라인의 가운데 숫자
#print(a,b,distance,mid)

molecule=1
denominator=a

for i in range(1,distance):
        molecule=molecule+1
        #분자
        denominator=denominator-1
        #분모


if((a%2==0)):
    print(molecule,"/",denominator,sep="")
else:
    print(denominator,"/",molecule,sep="")
    


---
7.달팽이는 올라가고 싶다(2869)
달팽이의 움직임을 계산하는 문제

푸는중
a,b,v=map(int,input().split())

date=1
total=0
while(1):
    total=total+a
    if(total>=v):
        break
    total=total-b
    date=date+1

print(date)

#while문 사용시 시간초과 -> 반복문 사용안하고 풀기


---

'''
