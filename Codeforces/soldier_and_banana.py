k, n, w = map(int, input().split())
total_banana_cost = 0
for i in range(1, w + 1):
    total_banana_cost += i * k

if total_banana_cost < n:
    print(0)
else:
    print(total_banana_cost - n)
