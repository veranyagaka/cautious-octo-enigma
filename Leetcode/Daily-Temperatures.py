1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        answer = [0] * len(temperatures)
4
5        stack = []
6
7        for i in range(len(temperatures)):
8
9            while stack and temperatures[stack[-1]] < temperatures[i]:
10                tmp = stack.pop()
11                answer[tmp] = i - tmp # update the next warmer day
12            
13            stack.append(i)
14
15        return answer
16
17        """
18        a2sv
19        use/store the indices instead
20        """