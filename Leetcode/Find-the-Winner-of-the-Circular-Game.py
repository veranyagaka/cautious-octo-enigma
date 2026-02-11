1class Solution:
2    def findTheWinner(self, n: int, k: int) -> int:
3
4        friends = list(range(1, n+1))
5        index = 0
6
7        while len(friends) > 1:
8            index = (index + k - 1) % len(friends) # including curr friend
9            friends.pop(index)
10
11        return friends[0]
12
13        
14
15        