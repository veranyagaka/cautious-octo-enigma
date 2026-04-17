1class StockSpanner:
2
3    def __init__(self):
4        self.arr = []
5        self.stack = []
6        
7
8    def next(self, price: int) -> int:
9        self.arr.append(price)
10        span = 1
11        while self.stack and self.stack[-1][0] <= price:
12            popped_span = self.stack[-1][1]
13            self.stack.pop()
14            span += popped_span
15        
16        self.stack.append([price, span])
17
18        return span
19
20        """
21        what does the stack store
22        """
23
24        
25
26
27# Your StockSpanner object will be instantiated and called as such:
28# obj = StockSpanner()
29# param_1 = obj.next(price)