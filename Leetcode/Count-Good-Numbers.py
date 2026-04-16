1class Solution:
2    def countGoodNumbers(self, n: int) -> int:
3        ## prime_numbers = [2, 3, 5, 7]
4        ## using recursion
5
6        MOD = 10 ** 9 + 7
7        ## how many positions
8        even_positions = (n+1) // 2
9        odd_positions = n // 2
10
11        return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD
12
13        """
14        5 choices for even indices
15        4 choices for odd indices
16        
17        """