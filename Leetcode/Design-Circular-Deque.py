1class MyCircularDeque:
2
3    def __init__(self, k: int):
4        self.capacity = k
5        self.size = 0
6        self.array = [0] * k
7        ## using pointers
8        self.front = 0
9        self.rear = -1
10        
11    ## using a circular array
12    def insertFront(self, value: int) -> bool:
13        if self.size >= self.capacity:
14            return False
15        ## supposed ot insert at front
16        self.front = (self.front - 1 + self.capacity) % self.capacity
17        self.array[self.front] = value
18
19        self.size += 1
20        return True
21
22        
23
24    def insertLast(self, value: int) -> bool:
25        if self.size >= self.capacity:
26            return False
27        
28        ## adding it to the end of the array
29        self.rear = (self.rear + 1 + self.capacity) % self.capacity
30
31        self.array[self.rear] = value
32        
33        self.size += 1
34        return True
35
36    def deleteFront(self) -> bool:
37        if self.size > 0:
38            ## self.array.remove(self.front)
39            self.front = (self.front + 1) % self.capacity
40
41            self.size -= 1
42            return True
43
44        return False
45
46        
47
48    def deleteLast(self) -> bool:
49        if self.size > 0:
50            ## self.array.remove(self.rear)
51            ## we are just moving the pointers
52            self.rear = (self.rear - 1) % self.capacity
53
54            self.size -= 1
55            return True
56
57        return False
58
59    def getFront(self) -> int:
60        if self.size > 0:
61            front_element = self.array[self.front]
62            return front_element
63
64        return -1
65        
66
67    def getRear(self) -> int:
68        if self.size > 0:
69            last_element = self.array[self.rear]
70            return last_element
71
72        return -1
73        
74
75    def isEmpty(self) -> bool:
76        if self.size == 0:
77            return True
78        return False
79        
80    def isFull(self) -> bool:
81        if self.size == self.capacity:
82            return True
83        return False
84
85
86    """
87    observations
88    """
89        
90
91
92# Your MyCircularDeque object will be instantiated and called as such:
93# obj = MyCircularDeque(k)
94# param_1 = obj.insertFront(value)
95# param_2 = obj.insertLast(value)
96# param_3 = obj.deleteFront()
97# param_4 = obj.deleteLast()
98# param_5 = obj.getFront()
99# param_6 = obj.getRear()
100# param_7 = obj.isEmpty()
101# param_8 = obj.isFull()