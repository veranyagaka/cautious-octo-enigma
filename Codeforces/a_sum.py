t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[-1] == sum(arr[:2]):
        print("YES")
    else:
        print("NO")
