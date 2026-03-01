1class Solution:
2    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
3        res = []
4        count = collections.Counter(arr1)
5        i = len(arr2)
6        for no in arr2:
7            if no in count.keys():
8                res.extend([no] * count[no])
9                del count[no]
10
11                # for times in range(count[no]):
12                #     res.append(no)
13        # remaining
14        for num in sorted(count.keys()):
15            res.extend([num] * count[num])
16
17        return res