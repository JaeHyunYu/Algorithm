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
2. 최댓값(2566)
최댓값을 2차원에서 찾는 문제

arr1=[[0 for j in range(9)] for i in range(9)]

a=b=0
max_v=0


for i in range(9):
    n=map(int,input().split())
    n=list(n)
    for j in range(9):
        if(max_v<=int(n[j])):
            max_v=int(n[j])
            a,b=(i+1),(j+1)
        arr1[i][j]=n[j]     

print(max_v)
print(a,b)

---
3. 세로읽기(10798)
문자열의 배열을 다루는 문제

arr=[]
mn=0

for i in range(5):
    arr.append(list(input()))
    if(len(arr[i])>=mn):
        mn=len(arr[i])
               


for i in range(mn):
    for j in range(5):
        if(len(arr[j])<=int(i)):
            continue
        else:
            print(arr[j][i],end=""

---
4. 색종이(2563)
2차원 배열을 활용하여 색종이로 평면을 덮는 문제



'''

