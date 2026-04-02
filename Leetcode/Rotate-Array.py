1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        # two pointers and a reversal trick
7        # [A | B] -> [B | A]
8        n = len(nums)
9
10        k = k % n
11
12
13        def reverse(l, r): # start, end
14            while l < r:
15                nums[l], nums[r] = nums[r], nums[l]
16                l += 1
17                r -= 1
18
19        reverse(0, n-1)
20        reverse(0, k-1)
21        reverse(k, n-1)
22        