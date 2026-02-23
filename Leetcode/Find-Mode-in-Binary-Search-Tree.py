1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findMode(self, root: Optional[TreeNode]) -> List[int]:
9        self.prev = None
10        self.result = []
11        self.count = 0
12        self.max_count = 0
13
14        def inorder(node):
15            if not node:
16                return
17            
18            inorder(node.left)
19
20            #process
21            if self.prev == node.val:
22                self.count += 1
23            else:
24                self.count = 1
25
26            if self.count > self.max_count:
27                self.max_count = self.count
28                self.result = [node.val]
29
30            elif self.count == self.max_count:
31                self.result.append(node.val)
32
33            self.prev = node.val
34
35
36            inorder(node.right)
37
38        inorder(root)
39        return self.result
40
41