1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        hashmap = {')': '(', ']':'[', '}': '{'}
5
6        for ch in s:
7            if ch in hashmap:
8                top_element = stack.pop() if stack else "#"
9
10                if top_element != hashmap[ch]:
11                    return False
12            else:
13                stack.append(ch)
14        
15        return not stack