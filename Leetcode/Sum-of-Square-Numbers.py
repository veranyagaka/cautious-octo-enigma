1class Solution:
2    def judgeSquareSum(self, c: int) -> bool:
3        ## two sum
4        ## search space = n ** .5 + 1
5
6        a = 0
7        b = int(c ** .5) + 1
8
9        while a <= b:
10            if c == a * a + b * b:
11                return True
12
13            elif a * a + b * b > c:
14                b -= 1
15
16            else:
17                a += 1
18
19        return False