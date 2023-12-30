Site:https://www.acmicpc.net/step/4
조건문

'''
1. 두 수 비교하기(1330)
두 수를 비교한 결과를 출력하는 문제

a,b=map(int,input().split())

if(a>b):
    print(">")
elif(a<b):
    print("<")
else: print("==")

---
2. 시험 성적(9498)
시험 점수를 성적으로 바꾸는 문제

a=int(input())
if(a>=90):
    print("A")
elif(a>=80):
    print("B")
elif(a>=70):
    print("C")
elif(a>=60):
    print("D")
else:
    print("F")

---
3. 윤년 (2753)
윤년을 판별하는 문제

a=int(input())
if((a%4==0) & (a%100!=0)):
    print(1)
elif((a%4==0) & (a%400==0)):
    print(1)
else:
    print(0)

---
4. 사분면 고르기(14681)
점이 어느 사분면에 있는지 알아내는 문제

a=int(input())
b=int(input())
if((a>0)&(b>0)):
    print(1)
elif((a>0)&(b<0)):
    print(4)
elif((a<0)&(b<0)):
    print(3)
else:
    print(2)

---
5. 알람 시계(2884)
시간 계산 문제

a,b=map(int,input().split())
if(b>=45):
    b=b-45
elif((a>0)):
    b=b+15
    a=a-1
else:
    b=b+15
    a=23
    
print(a,b)

---
6. 오븐 시계(2525)
범위가 더 넓은 시간 계산 문제

a,b=map(int,input().split())
c=int(input())
fin_hour=0
plus_hour=int(c/60)
plus_min=int(c%60)


if((b+plus_min)>=60):
    fin_min=b+plus_min-60
    plus_hour=plus_hour+1
else:
    fin_min=b+plus_min
    
if((a+plus_hour)>=24):
    fin_hour=a+plus_hour-24
else:
    fin_hour=a+plus_hour

print(fin_hour,fin_min)

---
7. 주사위 세개(2480)
조건에 따라 상금을 계산하는 문제

a=[1,2,3]

a[0],a[1],a[2]=map(int,input().split())



if((a[0]==a[1]==a[2])):
    print(10000+a[0]*1000)
elif((a[0]==a[1])):
    print(1000+a[0]*100)
elif((a[0]==a[2])):
    print(1000+a[0]*100)
elif((a[1]==a[2])):
    print(1000+a[1]*100)
else:
    d=a[0]
    for i in a:
        if i>d:
            d=i
    print(d*100)
    
'''
