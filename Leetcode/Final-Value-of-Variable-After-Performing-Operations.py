1class Solution:
2    def finalValueAfterOperations(self, operations: List[str]) -> int:
3        x = 0
4        for op in operations:
5            if '+' in op:
6                x += 1
7            else: 
8                x -=1
9
10        return x