a = int(input())
cnt = 0
for i in range(1,int(pow(a,1/2))):
    if(a % i == 0):
        cnt += 1
if(int(pow(a,1/2)) == pow(a,1/2)):
    print((cnt*2)+1)
else:
    print(cnt*2)
