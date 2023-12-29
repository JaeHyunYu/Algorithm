s=input()
n=int(input())

print(s[n-1])

---

s=input()


print(len(s))

---

n=int(input())

for i in range(n):
    s=input()
    print(s[0],s[len(s)-1],sep="")

---

n=int(input())

for i in range(n):
    s=input().split()
    a=int(s[0])
    st=s[1]
 
    for j in range(len(st)):
        print(a*st[j],end="")
    print("")

---

s=input().split()

print(len(s))

---

n,m=map(int,input().split())

n=(int(n/100)+int(int(n/10)%10)*10+(n%10)*100)
m=(int(m/100)+int(int(m/10)%10)*10+(m%10)*100)

print(max(n,m))

---
s=input()
total=0


for i in range(len(s)):
    total=total+(int((ord(s[i])-ord("A"))/3)+3)

print(total)

---

s=input()
total=0


for i in range(len(s)):
    num=int((ord(s[i])-ord("A"))/3)+3
    if(ord(s[i])>=ord("S"))):
        tmp=s[i]-
    total=total+num

print(total)
#진행중
