1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        count = 0
4        
5        def is_prime(n):
6            if n <= 1:
7                return False
8            if n == 2:
9                return True
10            if n % 2 == 0:
11                return False
12
13            for i in range(3, int(n**0.5) + 1, 2):
14                if n % i == 0:
15                    return False
16
17            return True
18        for num in range(left, right+1):
19            bin_no = bin(num)[2:]
20            if is_prime(bin_no.count("1")):
21                count += 1
22
23        return count