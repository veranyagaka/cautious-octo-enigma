1class Solution:
2    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
3        ## counting sort
4        max_height = max(heights)
5        count = [""] * (max_height + 1)
6        result = []
7
8        """index = height
9        value = name
10        """
11        for i in range(len(heights)):
12            count[heights[i]] = names[i]
13
14        for h in range(max_height, -1, -1): # descending order
15            if count[h] != "":
16                result.append(count[h])
17        
18        return result