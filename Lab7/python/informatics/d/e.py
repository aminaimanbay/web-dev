n = int(input())
a = input().split()
for i in range(0,len(a)-1):
    if(int(a[i]) > 0 and int(a[i+1]) > 0):
        print("YES")
        quit()
    if(int(a[i]) < 0 and int(a[i+1]) < 0):
        print("YES")
        quit()
print("NO")
