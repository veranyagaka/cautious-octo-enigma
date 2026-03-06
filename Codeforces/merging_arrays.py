# two pointers
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []

first, second = 0, 0

while first < len(a) and second < len(b):
    if a[first] < b[second]:
        res.append(a[first])
        first += 1
        
    else:
        res.append(b[second])
        second += 1
        
res.extend(a[first:])
res.extend(b[second:])


print(*res)