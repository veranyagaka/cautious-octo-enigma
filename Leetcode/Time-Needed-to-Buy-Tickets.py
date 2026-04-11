1class Solution:
2    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
3
4        ans = 0
5
6        for i in range(len(tickets)):
7            if i <= k:
8                ans += min(tickets[i], tickets[k])
9            else:
10                ans += min(tickets[i], tickets[k] - 1) 
11
12        return ans
13
14        """
15        formulae
16        i > k:
17        they miss the last round cos k is done
18        """