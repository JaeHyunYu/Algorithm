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


---
3. 세탁소 사장 동혁(2720)
💰


---
4.중앙 이동 알고리즘(2903)
둘씩 반복해서 나눴을 때 점의 개수를 세는 문제



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
