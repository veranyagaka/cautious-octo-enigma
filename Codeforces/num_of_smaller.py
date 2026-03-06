n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
first = 0
for second in range(len(b)):
    while first < len(a) and a[first] < b[second]:
        first += 1
    
    res.append(first)

    
print(*res)