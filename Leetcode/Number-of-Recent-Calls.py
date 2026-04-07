1class RecentCounter:
2
3    def __init__(self):
4        self.queue = []
5        # self.count = 0
6        
7
8    def ping(self, t: int) -> int:
9        self.queue.append(t)
10
11        while self.queue[0] < (t - 3000):
12            self.queue.pop(0)
13
14        return len(self.queue)
15        
16
17
18# Your RecentCounter object will be instantiated and called as such:
19# obj = RecentCounter()
20# param_1 = obj.ping(t)