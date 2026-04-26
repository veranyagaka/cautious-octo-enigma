1class Solution:
2    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
3        
4        houses.sort()
5        heaters.sort()
6
7        ## using two pointers
8        j = 0
9        ans = 0
10
11        for i in range(len(houses)):
12            # close and next heater 
13            # distance from curr house
14            h = houses[i]
15            while j < len(heaters) - 1 and abs(heaters[j+1] - h) <= abs(heaters[j] - h):
16                j += 1
17
18            # closest_heater = ...
19
20            ans = max(ans, abs(heaters[j] - h))
21
22
23        return ans