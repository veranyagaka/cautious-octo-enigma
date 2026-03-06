n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
# print(a)
# print(a[:k])
# print(a[k])
if k == 0:
    res = a[0] -1
    print(res if res >= 1 else -1)
    
elif k == n:
    print(a[k-1])
else:
    if a[k-1] == a[k]:
        print(-1)
    else:
        print(a[k-1])
"""
pseudocode
7 4
3 7 5 1 10 3 20

7 2
3 7 5 1 10 3 20

"""

