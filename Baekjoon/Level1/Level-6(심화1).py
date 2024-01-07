'''
Site : https://www.acmicpc.net/step/52
심화1

1. 	새싹(25083)
🌱

print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")


---

2. 킹, 퀸, 룩, 비숍, 나이트, 폰(3003)
♟️

a=input().split()
b=[1,1,2,2,2,8]

for i in range(6):
    print(b[i]-int(a[i]),end=" ")

---
3. 	별 찍기 - 7(2444)
🌟

n=int(input())

for i in range(n):
    print(" "*(int((2*n-1-(2*(i+1)-1))/2)),end="")
    print("*"*(2*(i+1)-1))

for i in range(n-2,-1,-1):
    print(" "*(int((2*n-1-(2*(i+1)-1))/2)),end="")
    print("*"*(2*(i+1)-1))

---
4. 팰린드롬인지 확인하기(10988)
🔄

a=input()
count=0
for i in range(len(a)):
    if(a[i]==a[len(a)-1-i]):
        count=count+1
    else:
        break

if(count==len(a)):
    print(1)
else:
    print(0)

---
5. 단어공부(1157)
주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

import sys

s=sys.stdin.readline()
count=0
s=s.upper()
s=list(s)
d=[]


#for i in range(len(s)):
#    if(ord(s[i])>=97):
#        s[i]=chr(int(ord(s[i])-32))

#        ==upper과 같은 역할



s.sort()
print(s)

for i in range(len(s)):
    print(s[i])

del s[0]

print(s[0])

for i,r in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            count=count+1:
        else:
            i=j-1
            d[i]=count
            count=0
            
        
import sys

s=sys.stdin.readline()
count=0
incount=0
s=s.upper()
s=list(s)
board = [[0] * 2 for i in range(26)]


#for i in range(len(s)):
 #   if(ord(s[i])>=97):
 #       s[i]=chr(int(ord(s[i])-32))

 #       ==upper과 같은 역할

s.sort()
s.reverse()

i=0
while(i<len(s)):
     for j in range(i,len(s)):
        if(s[i]==s[j]):
            count=count+1
            continue
        else:
            i=j-1
            board[incount][0]=i
            board[incount][1]=count
            incount=incount+1
            count=0
            break
     i=i+1

count=0
flag=0

max=board[0][1]

for i in range(incount):
    if(max<=board[i][1]):
        max=board[i][1]
    else:
        continue

for i in range(incount):
    if(max<=board[i][1]):
        count=count+1
        flag=i
    else:
        continue

if(count>1):
    print("?")
else:
    print(s[board[flag][0]])



---

6. 크로아티아 알파벳(2941)
두세 문자가 한 글자로 묶일 수 있을 때 글자의 수를 세는 문제



for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            count=count+1
    d.append(count)
    count=0

for i in range(len(d)):
    if(max(d)==d[i]):
        count=count+1
        flag=i
    else:
        continue

if(count==1):
    print(s[flag])
else:
    print("?")

    ---

    a=["c=","c-","dz=","d-","lj","nj","s=","z="]
s=input()
for i in range(len(a)):
    s=s.replace(a[i],"*")
print(len(s))

---
7. 그룹 단어 체커(1316)
조건에 맞는 문자열을 찾는 문제

n=int(input())
count=0


for j in range(n):
    s=input()
    s=list(s)
    a=list(set(s))

    for i in range(len(a)):
        flag=0
        num=s.count(a[i])
        locate=s.index(a[i])
        for k in range(num):
            if(s[locate]!=s[locate+k]):
                count=count+1
                flag=1
                break
            else:
                continue
        if(flag==1):
            break
        else:
            continue

    
print(n-count)


---
8. 너의 평점은(25206)
열심히 문제를 푸시는 여러분은 A+입니다

def cal(param1):
    if(param1=='A+'):
        return float(4.5)
    elif(param1=='A0'):
        return float(4.0)
    elif(param1=='B+'):
        return float(3.5)
    elif(param1=='B0'):
        return float(3.0)
    elif(param1=='C+'):
        return float(2.5)
    elif(param1=='C0'):
        return float(2.0)        
    elif(param1=='D+'):
        return float(1.5)
    elif(param1=='D0'):
        return float(1.0)
    else:
        return 0



credit=0
grade=0

for i in range(20):
    s=input().split()
    if(s[2]=='P'):
        continue
    else:
        credit=credit+float(s[1])
        grade=grade+float(s[1])*cal(s[2])
        

print(round(grade/credit,6))

'''
