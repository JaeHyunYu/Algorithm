
'''
Site:https://www.acmicpc.net/step/22
브루트 포스
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

a,b,c,d,e,f=map(int,input().split())

if((a==0) & (b==0)):
    print(0,int(c/b))
elif((b==0)&(e==0)):
    print(int(c/a),0)
else:
    x=int((c*e-f*b)/(a*e-d*b))
    y=int((c*d-a*f)/(b*d-a*e))
    print(x,y)



---
4. 체스판 다시 칠하기 (1018)
체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제

n,m=map(int,input().split())

arr=[]

for i in range(n):
    arr.append(input())

WB= [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
]

BW=[
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"]

def chkwb(x,y):
    count=0
    count2=0
    for i in range(8):
        for j in range(8):
            if(arr[x+i][y+j]!=WB[i][j]):
                count=count+1
    for i in range(8):
        for j in range(8):
            if(arr[x+i][y+j]!=BW[i][j]):
                count2=count2+1
    return min(count,count2)


minv=chkwb(0,0)

for i in range(n-7):
    for k in range(m-7):
        if(minv>chkwb(i,k)):
            minv=chkwb(i,k)
  
print(minv)


---
5. 영화감독 숌(1436)
N번째 종말의 수가 나올 때까지 차례대로 시도하는 문제

n=int(input())
cnt=0
i=1
while(1):
    if(cnt==n):
        print(i)
        break
    i=i+1
    if '666' in str(i):
        cnt=cnt+1
    else:
        continue




---
6. 설탕 배달(2839)
한때는 이 문제가 "기본 수학 1" 단계에 있었지만, 사실 브루트 포스로 푸는 게 더 쉽습니다.

n=int(input())

#5x+3y=n
flag=0
x=int(n/5)


for i in range(x,-1,-1):
    if((n-5*i)%3==0):
        print(i+int((n-5*i)/3))
        flag=1
        break

if(flag==0):
    print(-1)


'''




