1class Solution:
2    def diffWaysToCompute(self, expression: str) -> List[int]:
3        ## neetcode help
4        ## we know we have to use recursion
5        """
6        observations
7        operations we are allowed to do
8        the integer values 
9        """
10        operations = {
11            "+": lambda x, y: x + y,
12            "-": lambda x, y: x - y,
13            "*": lambda x, y: x * y,
14        }
15        n = len(expression)
16
17        def backtrack(left, right):
18            res = []
19
20            for i in range(left, right+1):
21                op = expression[i]
22                if op in operations:
23                    num1 = backtrack(left, i-1)
24                    num2 = backtrack(i+1, right)
25
26                    for n1 in num1:
27                        for n2 in num2:
28                            res.append(operations[op](n1, n2))
29                    
30            if res == []:
31                res.append(int(expression[left:right+1]))
32
33            
34            return res
35
36
37        return backtrack(0, n - 1)