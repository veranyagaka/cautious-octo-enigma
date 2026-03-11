n, t = map(int, input().split())

a = list(map(int, input().split()))

# sliding window and two pointers
left = 0
window_size = 0
curr_sum = 0
for right in range(n):
    curr_sum += a[right]
    while curr_sum > t:
        curr_sum -= a[left]
        left += 1

    window_size = max(window_size, right - left + 1)

print(window_size)