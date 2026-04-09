1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val, prev, next, child):
5        self.val = val
6        self.prev = prev
7        self.next = next
8        self.child = child
9"""
10
11class Solution:
12    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
13
14        # edgecase
15        if not head: return head
16        
17        stack = [head]
18        dummy = Node(0)
19
20        curr = dummy
21
22        while stack:
23            tmp = stack.pop() # the next node to process
24
25            if tmp.next: stack.append(tmp.next)
26            if tmp.child: stack.append(tmp.child)
27
28            curr.next = tmp
29
30            # point to the previous node
31            tmp.prev = curr 
32            tmp.child = None
33
34            curr = tmp
35
36            # make the child pointer NOne
37
38        head.prev = None
39        return head
40
41        """
42        using a stack to keep track of the next and the child nodes
43        you can also try and do it recursively
44        a guy on yt helped with this one
45        """