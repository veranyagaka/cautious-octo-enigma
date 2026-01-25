# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())
hash = {}
for _ in range(n):
    a, b = input().split()
    b = int(b)
    hash[a] = b

for x in sys.stdin:
    x = x.strip()
    if x in hash:
        print(x + "=" + str(hash[x]))
    else:
        print("Not found")
"""
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

output:
sam=99912222
Not found
harry=12299933
"""
