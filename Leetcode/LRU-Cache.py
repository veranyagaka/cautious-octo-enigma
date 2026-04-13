1class Node:
2    def __init__(self, key=0, val=0, next = None, prev = None):
3        self.key = key
4        self.val = val
5        self.next = next
6        self.prev = prev
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        ## doubly linked list
12        self.head = Node(-1, -1)
13        self.tail = Node(-1, -1)
14        self.head.next = self.tail
15        self.tail.prev = self.head
16
17        self.capacity = capacity
18        self.size = 0
19        self.cache = {}
20        
21
22    def get(self, key: int) -> int:
23        if key not in self.cache:
24            return -1
25
26        ## move to be head
27        ## TODO
28        node = self.cache[key]
29        self.move_to_head(node)
30        return node.val
31        
32
33    def put(self, key: int, value: int) -> None:
34        if key in self.cache:
35            node = self.cache[key]
36            # update value
37            node.val = value
38            self.move_to_head(node)
39
40        else:
41            if self.size == self.capacity:
42                ## remove tail
43                last = self.remove_tail()
44                self.cache.pop(last.key)
45                self.size -= 1
46            
47            node = Node(key, value)
48            self.cache[key] = node
49            self.add_to_head(node)
50            self.size += 1
51
52    
53    ## helper functions
54    def move_to_head(self, node):
55        self.remove_node(node)
56        self.add_to_head(node)
57
58    def add_to_head(self, node):
59        ## review
60        node.next = self.head.next
61        node.prev = self.head
62        self.head.next = node
63        node.next.prev = node
64
65
66    def remove_tail(self):
67        node = self.tail.prev
68        self.remove_node(node)
69        return node
70
71
72    def remove_node(self, node):
73        node.prev.next = node.next
74        node.next.prev = node.prev
75
76    ## reference: https://leetcode.com/submissions/detail/1967167053/
77
78# Your LRUCache object will be instantiated and called as such:
79# obj = LRUCache(capacity)
80# param_1 = obj.get(key)
81# obj.put(key,value)