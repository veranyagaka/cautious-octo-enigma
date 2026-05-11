1class Solution:
2    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
3        
4        ## use binary search
5        ## if a spell and potion pair are successful then the spell and stronger potions will be successful too
6        import math
7
8        potions.sort()
9        # s_spells = sorted(spells)
10
11        res = []
12        n = len(potions)
13
14        def look_for_i(num, arr, success):
15            low = 0
16            high = len(arr) - 1
17            res = len(arr)
18
19            while low <= high:
20                mid = (low + high) // 2
21                # if arr[mid] == target:
22                #     return mid
23
24                if arr[mid] * num >= success:
25                    res = mid
26                    high = mid - 1
27
28                else:
29                    low = mid + 1
30
31            return res  # the lowest index in the arr that is suitable
32
33        for i, num in enumerate(spells):
34            pairs = 0
35            ## supposed to avoid division at all costs
36            ## target = math.ceil(success / num) 
37
38            i = look_for_i(num, potions, success)
39
40            pairs += n - i
41
42            # for i, x in enumerate(potions):
43
44            #     ## use binary search here
45            #     if num * x >= success:
46            #         pairs += n - i
47            #         break
48
49            res.append(pairs)
50
51        return res
52                    