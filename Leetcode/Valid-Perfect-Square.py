1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        
4        ## supposed to use binary search
5        if num == 1:
6            return True
7
8        ## think about what the possible highest and lowest no could be
9        ## the smallest and possbile largest candidates
10        low = 1
11        high = num // 2
12
13        while low <= high:
14            mid = (low + high) // 2
15            curr = mid * mid
16
17            if curr == num:
18                return True
19
20            elif curr > num:
21                high = mid - 1
22
23            else:
24                low = mid + 1
25
26        return False
27