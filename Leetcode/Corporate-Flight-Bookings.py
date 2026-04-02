1class Solution:
2    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
3        # prefix sum boi
4
5        ans = [0] * (n+1)
6        diff = [0] * (n+1)
7        run_sum = 0
8        
9        # 1 based indexing
10        for first, last, seats in bookings:
11            # mark start and end +ve and -ve
12            diff[first - 1] += seats
13            diff[last] -= seats
14
15        for i, num in enumerate(diff):
16            run_sum += num
17            ans[i] = run_sum
18
19        return ans[:n]