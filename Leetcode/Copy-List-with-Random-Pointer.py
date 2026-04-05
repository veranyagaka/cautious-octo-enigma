1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        # neetcode help
13        ## two passes: one for the node creation, second for the pointers
14        curr = head
15        oldToCopy = {None:None}
16
17        while curr:
18            copy = Node(curr.val)
19            oldToCopy[curr] = copy
20            curr = curr.next
21
22        curr = head
23
24        while curr:
25            copy = oldToCopy[curr]
26            copy.next = oldToCopy[curr.next]
27            copy.random = oldToCopy[curr.random]
28
29            curr = curr.next
30
31
32        return oldToCopy[head]