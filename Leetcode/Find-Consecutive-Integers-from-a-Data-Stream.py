1class DataStream:
2
3    def __init__(self, value: int, k: int):
4        self.value = value
5        self.k = k
6        self.count = 0
7        
8
9    def consec(self, num: int) -> bool:
10        if num == self.value:
11            self.count += 1
12        else:
13            self.count = 0
14
15        return self.count >= self.k
16
17    """
18    using count is more optimal
19    """
20
21
22# Your DataStream object will be instantiated and called as such:
23# obj = DataStream(value, k)
24# param_1 = obj.consec(num)