a = int(input())
i = 0
while i < a+1:
    if pow(2,i)<=a:
        print(pow(2,i),end=' ')
    i+=1
