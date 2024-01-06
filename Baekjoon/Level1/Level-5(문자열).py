Site : https://www.acmicpc.net/step/7
문자열


'''
1. 문자와 문자열(27866)
문자열을 입력받고 문자열의 특정 위치를 읽어 봅시다.

s=input()
n=int(input())

print(s[n-1])

---
2. 단어 길이 재기(2743)
문자열을 입력받고 길이를 재는 문제

s=input()
print(len(s))

---
3. 문자열(9086)
문...제

n=int(input())

for i in range(n):
    s=input()
    print(s[0],s[len(s)-1],sep="")

---


7. 문자열 반복(2675)
데이터는 결국 0과 1일 텐데 문자를 어떻게 만드는 걸까요? 아스키 코드에 대해 알아봅시다.

n=int(input())

for i in range(n):
    s=input().split()
    a=int(s[0])
    st=s[1]
 
    for j in range(len(st)):
        print(a*st[j],end="")
    print("")

---
8. 단어의 개수(1152)
정수를 문자열로 입력받는 문제. Python처럼 정수 크기에 제한이 없다면 상관 없으나, 예제 3은 일반적인 정수 자료형에 담기에 너무 크다는 점에 주목합시다.

s=input().split()

print(len(s))

---
9. 상수(2908)
숫자를 뒤집어서 비교하는 문제

n,m=map(int,input().split())

n=(int(n/100)+int(int(n/10)%10)*10+(n%10)*100)
m=(int(m/100)+int(int(m/10)%10)*10+(m%10)*100)

print(max(n,m))

---
7. 문자열 반복(2675)
각 문자를 반복하여 출력하는 문제

s=input()
total=0


for i in range(len(s)):
    total=total+(int((ord(s[i])-ord("A"))/3)+3)

print(total)

---
10. 다이얼(5622)
규칙에 따라 문자에 대응하는 수를 출력하는 문제
s=input()
total=0


for i in range(len(s)):
    num=int((ord(s[i])-ord("A"))/3)+3
    if(ord(s[i])>=ord("S")):
        num=int((ord(s[i])-1-ord("A"))/3)+3
      
    if(ord(s[i])>=ord("Z")):
        num=int((ord(s[i])-2-ord("A"))/3)+3
      
    total=total+num

print(total)

---
11. 그대로 출력하기(11718)
그대로 출력하기

while(1):
    try:
        a=input()
        print(a)
    except:
        break
