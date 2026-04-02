t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    min_cost = 0

    l = 0
    r = n - 1

    for x in b:
        if l > r or r - l + 1 < x:
            break
        # edge case
        if x == 1:
            l += 1 # the item is free
            continue
        

        # the group size is x
        for _ in range(x-1):
            min_cost += a[r]
            r -= 1


        l += 1 # cheapest item becoming free

    while l <= r:
        min_cost += a[l]
        l += 1
    print(min_cost)
