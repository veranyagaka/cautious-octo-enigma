1class Solution:
2    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
3        # prefix sum boi
4
5        ans = [0] * n
6        diff = [0] * n
7        run_sum = 0
8        
9        # 1 based indexing
10        for first, last, seats in bookings:
11            # mark start and end +ve and -ve
12
13            if last == n:
14                diff[first - 1] += seats
15                # we do not minus
16            else:
17                diff[first - 1] += seats
18                diff[last] -= seats
19
20        for i, num in enumerate(diff):
21            run_sum += num
22            ans[i] = run_sum
23
24        return ans