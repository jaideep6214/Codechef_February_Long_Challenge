t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    l=input()
    l=list(map(int,l.split()))
    l.sort()
    dist=[]
    ans.append(2*(abs(l[0]-l[n-1])))
for i in ans:
    print(i)
        
