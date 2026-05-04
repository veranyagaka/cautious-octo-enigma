1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def countNodes(self, root: Optional[TreeNode]) -> int:
9        ## less than o(n) TC
10        ## compute the height of left and right
11        ## if equal = formula
12        ## else just traverse on the side that aint perfect
13
14        if not root: return 0
15
16        def get_left_height(node):
17            height = 0
18            while node:
19                height += 1
20                node = node.left
21
22            return height
23
24        def get_right_height(node):
25            height = 0
26            while node:
27                height += 1
28                node = node.right
29
30            return height
31
32        left_h = get_left_height(root)
33        right_h = get_right_height(root)
34
35        if left_h == right_h:
36            return (2 ** left_h)- 1
37
38        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
39
40
41
42            
43
44
45        # left = self.countNodes(root.left)
46        # right = self.countNodes(root.right)
47
48        # return 1 + left + right 