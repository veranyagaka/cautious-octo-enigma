1class Solution:
2    def dividePlayers(self, skill: List[int]) -> int:
3        # two pointers
4        # pair smallest with largest since we need a size of two
5
6        skill.sort()
7        l, r = 0, len(skill) -1    
8
9        target = skill[0] + skill[-1]
10
11        ans = 0
12
13        while l < r:
14            if skill[l] + skill[r] != target:
15                return -1
16
17            ans += skill[l] * skill[r]
18
19            l += 1
20            r -= 1
21
22        return ans
23