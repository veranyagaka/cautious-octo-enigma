1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        ## using a stack and simulation
4
5        stack = []
6
7        for a in asteroids:
8            # case 1
9            if a < 0: 
10
11                while stack and stack[-1] < abs(a) and stack[-1] > 0: # edge case for 2 negative nos
12                    stack.pop()
13
14                ## if top of the stack is negative
15                
16                ## case 2 exactly equal
17                if stack and abs(a) == stack[-1]:
18                    stack.pop() # remove 8
19                    continue # do not append -8
20
21                if not stack or stack[-1] < 0: # possibility a negative value can enter stack and edge case for 2 negative nos - > or stack[-1] < 0:
22                    stack.append(a)
23                # else:
24                #     continue
25
26            else:
27                stack.append(a)
28
29        return stack
30
31        """
32        order of execution matters
33        smaller ones can be crushed then equal comes in later
34        5 10 -5
35        add 5 to stack
36
37        the condition is when its negative and greater
38        ---
39
40
41        """