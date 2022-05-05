T=int(input())
for i in range(T):
    d,m,y=map(int,input().split("/"))
    t=[0,3,2,5,0,3,5,1,4,6,2,4]
    y-=m<3
    k=(y+int(y/4)-int(y/100)+int(y/400)+t[m-1]+d)%7
    l=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    print(l[k])
