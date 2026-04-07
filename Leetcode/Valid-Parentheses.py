1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        hashmap = {"{": "}", "[": "]", "(": ")"}
5
6        for ch in s:
7            if ch in hashmap:
8                stack.append(ch)
9            else:
10                if len(stack) == 0:
11                    return False
12
13                pop_element = stack.pop()
14                if hashmap[pop_element] != ch:
15                    return False
16
17        return not stack
18        
19        """
20        a2sv
21        approach if
22        we come accross an opening we add it to the stack
23        else we pop and check 
24        edge cases; stack is empty or not
25        there must be closed if not false 
26        """