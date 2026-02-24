1class Solution:
2    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
3        ## selection sort
4        n = len(heights)
5
6        for i in range(n):
7            min_index = i
8
9            # this is to find the minimum no
10            for j in range(i+1, n): 
11                if heights[j] > heights[min_index]: # cos its descenting
12                    min_index = j
13
14            # swap
15            heights[i], heights[min_index] = heights[min_index], heights[i]
16            names[i], names[min_index] = names[min_index], names[i]
17
18        return names