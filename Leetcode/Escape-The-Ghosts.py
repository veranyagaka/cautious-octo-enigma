1class Solution:
2    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
3        def get_turns(smth, target):
4            return abs(smth[0] - target[0]) + abs(smth[1] - target[1])
5
6        you_turns = get_turns([0, 0], target)
7
8        ghost_turns = []
9
10        for ghost in ghosts:
11            ghost_turn = get_turns(ghost, target)
12            ghost_turns.append(ghost_turn)
13
14        return min(ghost_turns) > you_turns