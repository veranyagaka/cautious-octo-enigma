1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        
5        boats = 0
6        n = len(people)
7        l = 0
8        r = n -1
9        
10        while l <= r and r < n:
11
12            if people[l] + people[r] > limit:
13                boats += 1
14                r -= 1
15
16            else: #people[l] + people[r] <= limit
17                boats += 1
18                r -= 1
19                l +=1
20            
21        return boats