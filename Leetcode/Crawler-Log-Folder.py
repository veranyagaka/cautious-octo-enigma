1class Solution:
2    def minOperations(self, logs: List[str]) -> int:
3        length = 0
4
5        for log in logs:
6            if log == "../":
7                if length > 0:
8                    length -= 1
9            elif log == "./":
10                continue            
11            else:
12                length += 1
13
14        return length