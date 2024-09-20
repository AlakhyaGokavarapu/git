size=int(input())
list=list(map(int,input().split()))
for i in range(1,size+1):
    if list.count(i)==0:
        print(i)
        break