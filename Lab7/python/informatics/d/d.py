n = int(input())
a = input().split()
cnt=0
for i in range(0,len(a)-1):
    if(int(a[i+1]) > int(a[i])):
        cnt +=1
print(cnt)
