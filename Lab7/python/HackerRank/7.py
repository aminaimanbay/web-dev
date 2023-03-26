a = int(input())
ar = set(input().split())
b = int(input())
br = set(input().split())

s = ar.difference(br)
print(len(s))
