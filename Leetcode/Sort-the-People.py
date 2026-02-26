1class Solution:
2    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
3        ## insertion sort
4        n = len(heights)
5
6        for i in range(1, n): # first element is always considered sorted
7            key_height = heights[i]
8            key_name = names[i]
9
10            j = i -1
11
12            while j >= 0 and heights[j] < key_height: # descending
13                # move
14                heights[j+1] = heights[j]
15                names[j+1] = names[j]
16                j -= 1
17
18            heights[j+1] = key_height
19            names[j+1] = key_name
20
21
22        return names