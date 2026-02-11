1class Solution:
2    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
3        seats.sort()
4        students.sort()
5        total = 0
6
7        for i in range(len(seats)):
8            val = abs(seats[i] - students[i])
9            total += val
10
11        return total
12
13