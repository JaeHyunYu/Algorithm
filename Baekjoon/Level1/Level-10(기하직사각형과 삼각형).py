Site:https://www.acmicpc.net/step/50

기하: 직사각형과 삼각형


'''
1. 직사각형 (27323)
직사각형의 넓이를 구하는 문제

a=int(input())
b=int(input())

print(a*b)

---
2. 직사각형에서 탈출 (1085)
직사각형과 점의 거리를 구하는 문제

x,y,w,h=map(int,input().split())
print(min(abs(w-x),x,abs(h-y),y))

---
3. 네 번째 점(3009)
직사각형을 완성하는 문제
arr=[[0 for i in range(2)] for i in range(4)]

for i in range(3):
    arr[i][0],arr[i][1]=map(int,input().split())

if(arr[0][0]==arr[1][0]):
    xdis=abs(arr[0][0]-arr[2][0])
    sx=arr[2][0]
else:
    xdis=abs(arr[0][0]-arr[1][0])
    if(arr[0][0]==arr[2][0]):
        sx=arr[1][0]
    else:
        sx=arr[0][0]

if(arr[0][1]==arr[1][1]):
    xdis=abs(arr[0][1]-arr[2][1])
    sy=arr[2][1]
else:
    ydis=abs(arr[0][1]-arr[1][1])
    if(arr[0][1]==arr[2][1]):
        sy=arr[1][1]
    else:
        sy=arr[0][1]


print(sx,sy)

---
4. 수학은 체육과목 입니다(15894)
피라미드 모양 도형의 둘레를 구하는 문제

a=int(input())
print(int(4*a))

---
5. 대지(9063)
옥구슬을 모두 포함하는 직사각형을 찾는 문제
n=int(input())


sx,sy=0,0
for i in range(n):
    a,b=map(int,input().split())
    if(i==0):
        bx,by=a,b
        sx,sy=a,b
    if(a>bx):
        bx=a
    if(a<sx):
        sx=a
    if(b>by):
        by=b
    if(b<sy):
        sy=b
print((bx-sx)*(by-sy)) 

---
6. 삼각형외우기(10101)
각도를 보고 삼각형을 판별하고 분류하는 문제

a=int(input())
b=int(input())
c=int(input())

if((a+b+c)==180):
    if(a==b==c==60):
        print("Equilateral")
    elif((a==b) | (a==c) | (b==c)):
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
    
---
7. 삼각형과 세변(5073)
변의 길이를 보고 삼각형을 판별하고 분류하는 문제
while(1):
    a,b,c=map(int,input().split())

    if(a==b==c==0):
        break
    maxa=max(a,b,c)

    if(maxa>=(a+b+c-maxa)):
        print("Invalid")
    else:
        if(a==b==c):
            print("Equilateral")
        elif((a==b) | (a==c) | (b==c)):
            print("Isosceles")
        else:
            print("Scalene")

---
8. 세 막대(14215)
가능한 한 둘레가 긴 삼각형을 만드는 문제
a,b,c=map(int,input().split())

maxa=max(a,b,c)
if(maxa==a):
    a=c
elif(maxa==b):
    b=c


                
if(maxa>=(a+b)):
    print(a+b+a+b-1)
else:
    print(maxa+a+b)

'''
