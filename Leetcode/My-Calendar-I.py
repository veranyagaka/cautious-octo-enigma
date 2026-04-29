1## neetcode help
2# using binary search tree
3"""
410, 20 if greater right child 
5if less left child 
6otherwise there is an overlap return false
7
8"""
9class Tree:
10    def __init__(self, start,end):
11        self.left = None
12        self.right = None
13        self.start = start
14        self.end = end
15
16    def insert(self, start,end):
17        curr = self
18
19        while True:
20            if start >= curr.end:
21                if not curr.right:
22                    curr.right = Tree(start,end)
23                    return True
24
25                curr = curr.right
26
27            elif end <= curr.start: 
28                if not curr.left:
29                    curr.left = Tree(start,end)
30                    return True
31
32                curr = curr.left
33
34            else:
35                return False
36        """
37        say we have 5 9 10 20 
38        """
39
40class MyCalendar:
41
42    def __init__(self):
43        self.root = None
44        
45
46    def book(self, startTime: int, endTime: int) -> bool:
47        if not self.root:
48            self.root = Tree(startTime, endTime)
49            return True
50
51        return self.root.insert(startTime, endTime)
52        
53
54
55# Your MyCalendar object will be instantiated and called as such:
56# obj = MyCalendar()
57# param_1 = obj.book(startTime,endTime)