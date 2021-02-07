def time_convert(time):
    if (time[6:]=="AM"):
        if (time[:2]=="12"):
            return ([0,int(time[3:5])])
        else:
            return ([int(time[:2]),int(time[3:5])])
    else:
        if (time[:2]=="12"):
            return ([int(time[:2]),int(time[3:5])])
        else:
            return ([int(time[:2])+12,int(time[3:5])])
        
    
    


t=int(input())
ans=[]
for i in range(t):
    time_to_check=input()
    time_to_check=time_convert(time_to_check)
    n=int(input())
    temp=""
    for y in range(n):
        l=input()
        time_start=l[0:8]
        time_end=l[9:]

        time_start=time_convert(time_start)
        time_end=time_convert(time_end)
        if (time_start[0]>time_end[0] or (time_start[0]==time_end[0] and time_start[1]>time_end[1])):
            if (time_to_check[0]<time_end[0] or time_to_check[0]>time_start[0] ):
                temp=temp+"1"
            elif(time_to_check[0]>time_end[0] and time_to_check[0]<time_start[0] ):
                temp=temp+"0"
            elif((time_to_check[0]==time_end[0] and time_to_check[1]<=time_end[1]) or (time_to_check[0]==time_start[0] and time_to_check[1]>=time_end[1])) :
                temp=temp+"1"
            else:
                temp=temp+"0"
        else:
            if (time_to_check[0]<time_start[0] or time_to_check[0]>time_end[0] ):
                temp=temp+"0"
            elif(time_to_check[0]>time_start[0] and time_to_check[0]<time_end[0] ):
                temp=temp+"1"
            elif((time_to_check[0]==time_start[0] and time_to_check[1]<time_start[1]) or (time_to_check[0]==time_end[0] and time_to_check[1]>time_end[1])) :
                temp=temp+"0"
            else:
                temp=temp+"1"
        
    ans.append(temp)

for i in ans:
    print(i)
