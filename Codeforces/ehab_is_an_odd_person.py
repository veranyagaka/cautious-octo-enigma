n = int(input())
a = list(map(int, input().split()))

has_even, has_odd = False, False

for num in a:
    if num % 2 == 0:
        has_even = True
        
    else:
        has_odd = True
        
if has_even and has_odd:
    a.sort()
    
print(*a)
"""
for i in range(n-1):
    
    if a[i] > a[i+1] and (a[i] + a[i+1]) % 2 == 1:
        a[i], a[i+1] = a[i+1], a[i]
     
print(*a)
"""   

"""think in parity:
    odd = odd + even
    fully evens or odds no swaps will happen"""