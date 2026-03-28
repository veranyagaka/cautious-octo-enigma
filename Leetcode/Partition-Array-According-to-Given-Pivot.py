1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        ans = []
4        left, right, same = [], [], []
5        a = nums
6        n = len(nums)
7
8        for i in range(n):
9            if a[i] == pivot:
10                same.append(a[i])
11            elif a[i] < pivot:
12                left.append(a[i])
13            else:
14                right.append(a[i])
15        ans = left+ same + right
16        return ans