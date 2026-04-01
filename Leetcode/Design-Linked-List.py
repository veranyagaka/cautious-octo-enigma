1class Node:
2    def __init__(self, val):
3        self.val = val
4        self.next = None
5
6
7class MyLinkedList:
8
9    def __init__(self):
10        self.head = None
11        self.size = 0
12        
13
14    def get(self, index: int) -> int:
15        if index < 0 or index >= self.size:
16            return -1
17            
18        curr = self.head
19        for _ in range(index):
20            curr = curr.next
21
22        return curr.val       
23
24    def addAtHead(self, val: int) -> None:
25        new_node = Node(val)
26
27        # if not self.head:
28        #     return new_node
29        
30        new_node.next = self.head
31        self.head = new_node
32        self.size += 1
33
34    def addAtTail(self, val: int) -> None:
35        new_node = Node(val)
36
37        if self.head is None:
38            self.head = new_node
39        else:
40            curr = self.head
41            while curr.next:
42                curr = curr.next
43            curr.next = new_node
44        self.size += 1
45
46    def addAtIndex(self, index: int, val: int) -> None:
47        if index > self.size or index < 0:
48            return
49        if index == 0:
50            self.addAtHead(val)
51
52        elif index == self.size:
53            self.addAtTail(val)
54
55        else:
56            new_node = Node(val)
57            curr = self.head
58            for _ in range(index-1): # stop just before the index
59                curr = curr.next
60            new_node.next = curr.next
61            curr.next = new_node
62
63            self.size += 1
64        
65
66    def deleteAtIndex(self, index: int) -> None:
67        if index < 0 or index >= self.size:
68            return
69
70        if index == 0:
71            self.head = self.head.next
72
73        else:
74            curr = self.head
75            for _ in range(index-1):
76                curr = curr.next
77            curr.next = curr.next.next
78
79        self.size -= 1
80
81        
82
83
84# Your MyLinkedList object will be instantiated and called as such:
85# obj = MyLinkedList()
86# param_1 = obj.get(index)
87# obj.addAtHead(val)
88# obj.addAtTail(val)
89# obj.addAtIndex(index,val)
90# obj.deleteAtIndex(index)