Site:https://www.acmicpc.net/step/3
반복문

'''
1. 구구단 (2739)
구구단을 출력하는 문제

a=int(input())
for i in range(1,10):
   print(a,"*",i,"=",a*i)

----
2. A+B - 3 (10950)
A+B를 여러 번 출력하는 문제

a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    print(b+c)
---
3. 합(8393)
1부터 N까지의 합을 구하는 문제. 물론 반복문 없이 풀 수도 있습니다.

n=int(input())
total=0
for i in range(1,(n+1)):
    total=total+i
print(total)

---
4. 영수증(25304)
💸

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
5. 코딩은 체육과목 입니다(25314)
코딩 공부를 잘 하여 이렇게 long long long long...을 칠판에 적는 일이 없도록 합시다.

a=int(input())
a=int(a/4)
print("long "*a,"int",sep="")

---
6. 빠른 A+B(15552)
빠르게 입력받고 출력하는 문제

import sys

n=int(sys.stdin.readline())

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)
    
---
7. A+B - 7(11021)
A+B를 조금 더 아름답게 출력하는 문제

a=int(input())
for i in range(1,(a+1)):
	b,c=map(int,input().split())
	print("Case #",i,": ",b+c,sep="")
---
8. A+B - 8(11022)
A+B를 바로 위 문제보다 아름답게 출력하는 문제
a=int(input())
for i in range(1,(a+1)):
	b,c=map(int,input().split())
	print("Case #",i,": ",b," + ",c," = ",b+c,sep="")
---
9. 별 찍기 - 1(2438)
별을 찍는 문제 1

a=int(input())
for i in range(1,(a+1)):
    print("*"*i)
---
10. 별 찍기 - 2(2439)
별을 찍는 문제 2

a=int(input())
for i in range(1,(a+1)):
    print(" "*(a-i),"*"*i,sep="")
---
11. A+B - 5(10952)
0 0이 들어올 때까지 A+B를 출력하는 문제

while(1):
    a,b=map(int,input().split())
    if(a==b==0):
        break
    print(a+b)

---
12. A+B - 4(10951)
입력이 끝날 때까지 A+B를 출력하는 문제. EOF에 대해 알아 보세요.

while(1):
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break

#EOF문제
'''
