t  = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    """REMOVE ELEMENTS FROM SMALLEST TO BIGGEST
    """
    arr.sort()
        
    possible = True
    for i in range(1, n):
        if arr[i] - arr[i-1] > 1:
            possible = False
            break
    
    print("YES" if possible else "NO")
    