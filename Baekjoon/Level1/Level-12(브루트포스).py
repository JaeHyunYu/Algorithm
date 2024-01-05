Site:https://www.acmicpc.net/step/22
브루트 포스
'''
---
1. 블랙잭(2798)
세 장의 카드를 고르는 모든 경우를 고려하는 문제

n,m=map(int,input().split())

arr=[]
arr=map(int,input().split())

arr=list(arr)

arr2=[]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if((arr[k]+arr[j]+arr[i])<=m):
                arr2.append(arr[k]+arr[j]+arr[i])
            else:
                continue

print(max(arr2))

---
2. 분해합(2231)
모든 경우를 시도하여 N의 생성자를 구하는 문제

n=int(input())


for i in range(1,n+1):
    total=i+sum(map(int,str(i)))
    if(total==n):
        print(i)
        break
if(i==n):
    print(0)



---
3. 수학은 비대면강의입니다(19532)
모든 x와 모든 y를 시도하여 해를 구하는 문제



---
4. 체스판 다시 칠하기 (1018)
체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제



---
5. 영화감독 숌(1436)
N번째 종말의 수가 나올 때까지 차례대로 시도하는 문제



---
6. 설탕 배달(2839)
한때는 이 문제가 "기본 수학 1" 단계에 있었지만, 사실 브루트 포스로 푸는 게 더 쉽습니다.


'''
