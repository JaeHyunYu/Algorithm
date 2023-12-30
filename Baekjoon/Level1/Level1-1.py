Site : https://www.acmicpc.net/step/1
입출력과 사칙연산

'''
1. 사칙연산 (10869)
모든 연산 문제

a,b=input().split()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

---
2. 	??! (10926)
입출력을 응용하는 문제??!

a=input()
print(a+"??!")

----
3. 1998년생인 내가 태국에서는 2541년생?! (18108)
식을 직접 세워서 계산하는 문제

a= int(input())
print(a-543)
----

4. 나머지(10430)
네 개의 계산식을 계산하는 문제. 이 문제를 푼 다음에는 직접 입력을 만들어서 넣어 봅시다. 어떤 사실을 관찰할 수 있나요?

a,b,c=map(int,input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

----

5. 곱셈(2588)
빈 칸에 들어갈 수는?

a=int(input())
b=int(input())
b1=int(b/100)
b2=int((b-b1*100)/10)
b3=b-b1*100-b2*10

print(b3*a)
print(b2*a)
print(b1*a)
print(a*b)

----
6. 꼬마 정민(11382)
더 큰 수를 더하는 문제

a,b,c=map(int,input().split())
print(a+b+c)

----
7. 고양이 (10171)
\, ' 등의 문자에 주의하며 고양이를 출력하는 문제

print("\\    /\\")
print(" )  ( \') ")
print("(  /  ) ")
print(" \\(__)| ")
----
8. 개 (10172)
", `, \ 등의 문자에 주의하며 개를 출력하는 문제

print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

'''
