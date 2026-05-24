1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        
4        ## supposed to use two pointers
5        ## from right to left
6        l = len(num1) - 1
7        r = len(num2) - 1
8
9        ans = []
10        carry = 0
11
12        #both must finish
13        while l >= 0 or r >= 0:
14
15            digit1 = int(num1[l]) if l >= 0 else 0
16            digit2 = int(num2[r]) if r >= 0 else 0
17
18            add = digit1 + digit2 + carry
19
20            curr_sum = add % 10 ## get the last digit
21            carry = add // 10
22
23            ans.append(curr_sum) 
24
25            l -= 1
26            r -= 1
27
28        ## if the no is smaller treat it as zero
29
30        if carry:
31            ans.append(carry)
32        
33        ## reverse
34        return "".join(map(str, ans[::-1]))
35        # return "".join(ans)
36
37