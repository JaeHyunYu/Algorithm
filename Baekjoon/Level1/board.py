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
'''


