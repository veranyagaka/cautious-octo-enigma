1class Solution:
2    def judgeSquareSum(self, c: int) -> bool:
3        ## two sum
4        ## search space = n ** .5 + 1
5
6        a = 0
7        b = int(c ** .5) + 1 ## make sure its an integer
8
9        while a <= b:
10            curr = a * a + b * b
11            
12            if c == curr:
13                return True
14
15            elif curr > c:
16                b -= 1
17
18            else:
19                a += 1
20
21        return False