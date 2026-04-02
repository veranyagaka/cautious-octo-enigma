1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        max_no = 0
4        left = 0
5        n = len(fruits)
6        hash_map = {}
7        # keeping track of counts
8
9        for right in range(n):
10            hash_map[fruits[right]] = hash_map.get(fruits[right], 0) + 1
11
12            while len(hash_map) > 2:
13                hash_map[fruits[left]] -= 1
14
15                if hash_map[fruits[left]] == 0:
16                    del hash_map[fruits[left]]
17
18                left += 1
19
20            max_no = max(max_no, right - left + 1)
21
22        return max_no