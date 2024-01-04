Site:https://www.acmicpc.net/step/53
시간 복잡도


'''
1. 알고리즘 수업 - 알고리즘의 수행 시간 1(24262)
프로그램의 수행 시간을 분석해 봅시다.
print("1")
print("0")

#n 에 어떤 값이 입력되든, 내부 연산을 수행한 후 반환할 때 return A[i] 는 한번 수행 된다.
#n에 어떤 값이 입력 되든 한번만 수행하면 되는 코드이므로, n에 비례하는 알고리즘이 아니다.
#따라서 수행시간 또한 1이다.

---
2. 알고리즘 수업 - 알고리즘의 수행 시간 2(24263)
뒤로 갈수록 명령어의 정확한 실행 횟수를 구하기 까다로워질 것입니다. 그러나...
n=int(input())
print(n)
print("1")




---
3. 	알고리즘 수업 - 알고리즘의 수행 시간 3 (24264)
...실행 횟수가 "대략적으로" 얼마나 빨리 커지는지는 비교적 간단하게 알 수 있습니다. 이 문제들에서 출력의 두 번째 줄이 바로 그것입니다.
import math
n=int(input())
print(int(math.pow(n,2)))
print("2")


---
4. 알고리즘 수업 - 알고리즘의 수행 시간 4 (24265)
n이 커질수록 n과 n²의 차이는 어마어마하게 벌어지기 때문에,

n=int(input())

print(int(n*(n-1)/2))
print(2)

# 1~(n-1)까지의 합! 등차수열 혹은 시그마 원리 이용


---
5.알고리즘 수업 - 알고리즘의 수행 시간 5 (24266)
"대략적으로"만 파악해도 자신의 코드가 시간 초과가 날 지 아닐지를 어느 정도 예측할 수 있습니다.

n=int(input())

print(int(n*n*n))
print(3)


---
6.알고리즘 수업 - 알고리즘의 수행 시간 6 (24267)
그 역할을 하는 것이 바로 시간 복잡도입니다.
n=int(input())

total=n*(n-1)*(n-2)/6

print(int(total))
print(3)

#nC3과 같은 원리
---
7.알고리즘 수업 - 점근적 표기 1 (24313)
시간 복잡도는 빅-O 표기법으로 표현할 수 있습니다. 정확한 정의보다는 "이 함수에 비례한다" 정도만 기억해도 무방합니다.

a1,a0=map(int,input().split())
c=int(input())
n0=int(input())

if(c>a1):
    if(n0>=(a0/(c-a1))):
        print(1)
    else:
        print(0)
elif(c==a1):
    if(a0<=0):
        print(1)
    else:
        print(0)
else: #c>a1이 되는 순간 오류 발생 - 값이 생길 수 밖에 없는 구조.
    print(0)


'''
