1class Solution:
2
3    def isPalindrome(self, x: int) -> bool:
4        # handle negarive numbers
5        if x < 0:
6            return False
7
8        reverse = 0
9        xcopy = x # save og to compare at the end
10
11        while x > 0:
12            reverse = (reverse * 10)  + (x % 10) # reverse digit by digit
13            x //=10
14        
15        return xcopy == reverse
16
17        