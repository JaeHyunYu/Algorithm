'''
a,b=map(int,input().split())

if(a>b):
    print(">")
elif(a<b):
    print("<")
else: print("==")

---
a=int(input())
if(a>=90):
    print("A")
elif(a>=80):
    print("B")
elif(a>=70):
    print("C")
elif(a>=60):
    print("D")
else:
    print("F")

---
a=int(input())
if((a%4==0) & (a%100!=0)):
    print(1)
elif((a%4==0) & (a%400==0)):
    print(1)
else:
    print(0)

---

a=int(input())
b=int(input())
if((a>0)&(b>0)):
    print(1)
elif((a>0)&(b<0)):
    print(4)
elif((a<0)&(b<0)):
    print(3)
else:
    print(2)

---

a,b=map(int,input().split())
if(b>=45):
    b=b-45
elif((a>0)):
    b=b+15
    a=a-1
else:
    b=b+15
    a=23
    
print(a,b)

---
a,b=map(int,input().split())
c=int(input())
fin_hour=0
plus_hour=int(c/60)
plus_min=int(c%60)


if((b+plus_min)>=60):
    fin_min=b+plus_min-60
    plus_hour=plus_hour+1
else:
    fin_min=b+plus_min
    
if((a+plus_hour)>=24):
    fin_hour=a+plus_hour-24
else:
    fin_hour=a+plus_hour

print(fin_hour,fin_min)

'''
a=[1,2,3]

a[0],a[1],a[2]=map(int,input().split())



if((a[0]==a[1]==a[2])):
    print(10000+a[0]*1000)
elif((a[0]==a[1])):
    print(1000+a[0]*100)
elif((a[0]==a[2])):
    print(1000+a[0]*100)
elif((a[1]==a[2])):
    print(1000+a[1]*100)
else:
    d=a[0]
    for i in a:
        if i>d:
            d=i
    print(d*100)
    
