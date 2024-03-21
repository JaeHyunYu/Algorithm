def solution(friends, gifts):
    al=[0 for i in range(len(friends))]
    arr1=[[0 for j in range(3)] for i in range(len(friends))]
    arr2=[[0 for j in range(len(friends))] for i in range(len(friends))]
    
    for j in range(len(gifts)):
        a,b=(gifts[j].split(' '))
        for i in range(len(friends)):
            if(a==friends[i]):            
                arr1[i][0]=arr1[i][0]+1
                for k in range(len(friends)):
                    if(b==friends[k]):
                        arr2[i][k]=arr2[i][k]+1
            if(b==friends[i]):
                arr1[i][1]=arr1[i][1]+1
                
    for j in range(len(friends)):
        arr1[j][2]=arr1[j][0]-arr1[j][1]
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if(i==j):
                continue
            else:
                if(arr2[i][j]>arr2[j][i]):
                    al[i]=al[i]+1
                elif(arr2[i][j]==arr2[j][i]):
                    if(arr1[i][2]>arr1[j][2]):
                        al[i]=al[i]+1
                    else:
                        continue


    
    answer = max(al)
    return answer
