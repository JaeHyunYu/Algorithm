'''
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")

---
while(1):
    try:
        a=input()
        print(a)
    except:
        break
---

a=input().split()
b=[1,1,2,2,2,8]

for i in range(6):
    print(b[i]-int(a[i]),end=" ")

---
n=int(input())

for i in range(n):
    print(" "*(int((2*n-1-(2*(i+1)-1))/2)),end="")
    print("*"*(2*(i+1)-1))

for i in range(n-2,-1,-1):
    print(" "*(int((2*n-1-(2*(i+1)-1))/2)),end="")
    print("*"*(2*(i+1)-1))

---

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
'''


import sys

s=sys.stdin.readline()
count=0
s=s.upper()
s=list(s)
d=[]

'''
for i in range(len(s)):
    if(ord(s[i])>=97):
        s[i]=chr(int(ord(s[i])-32))

        ==upper과 같은 역할
'''


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
            
        

'''
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
'''
