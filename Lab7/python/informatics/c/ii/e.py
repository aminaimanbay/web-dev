a = int(input())
i = 0
while i < a+1:
    if(pow(2,i)>=a):
        print(i)
        break
    i+=1
