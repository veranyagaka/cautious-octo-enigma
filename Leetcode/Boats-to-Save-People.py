1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        
5        boats = 0
6        running_sum = 0
7        n = len(people)
8        l = 0
9        r = n -1
10        
11        while l <= r and r < n:
12
13            if people[l] + people[r] > limit:
14                boats += 1
15                r -= 1
16
17            elif people[l] + people[r] <= limit:
18                boats += 1
19                r -= 1
20                l +=1
21            
22            else:
23                boats += 1
24                l += 1
25
26
27        return boats