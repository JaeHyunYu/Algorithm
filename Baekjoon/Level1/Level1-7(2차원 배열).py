Site: https://www.acmicpc.net/step/2
2차원 배열

'''
---
1. 행렬 덧셈(2738)
행렬을 2차원 배열로 만들어 더하는 문제

a,b=map(int,input().split())

arr1=[[0 for j in range(b)] for i in range(a)]
arr2=[[0 for j in range(b)] for i in range(a)]

for i in range(a):
    s=input().split()
    for j in range(b):
        arr1[i][j]=s[j]

for i in range(a):
    s=input().split()
    for j in range(b):
        arr2[i][j]=s[j]


for i in range(a):
    for j in range(b):
        print(int(arr1[i][j])+int(arr2[i][j]),end=" ")
    print()

---
'''

