a = int(input())
b = int(input())

for i in range(a,b+1):
    if(int(pow(i,1/2)) == pow(i,1/2)):
        print(i,end=" ")
