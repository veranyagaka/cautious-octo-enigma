1class MyCalendar:
2
3    def __init__(self):
4        self.arr = []
5        
6
7    def book(self, startTime: int, endTime: int) -> bool:
8        """
9        what does it mean to overlap
10        33 41 | 47 50
11        """
12        for s, e in self.arr:
13            if not (e <= startTime or endTime <= s):
14                return False
15        
16        self.arr.append((startTime, endTime))
17
18        return True
19
20"""
21[[],[10,20],[15,25],[20,30]]
22"""
23
24
25# Your MyCalendar object will be instantiated and called as such:
26# obj = MyCalendar()
27# param_1 = obj.book(startTime,endTime)