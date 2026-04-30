1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    ## 
9    def findMin(self, node):
10        while node.left:
11            node = node.left
12
13        return node
14
15    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
16
17        if not root:
18            return root
19
20        if key > root.val:
21            root.right = self.deleteNode(root.right, key)
22
23        elif key < root.val:
24            root.left = self.deleteNode(root.left, key)
25
26        else:
27            ## we have found the node to remove yay!
28            ## case 1 node not children
29            if not root.left and not root.right:
30                return None
31
32            ## one child only
33            if not root.left:
34                return root.right
35            
36            if not root.right:
37                return root.left
38
39            ## node has two children
40            successor = self.findMin(root.right)
41            root.val = successor.val
42
43            ## remember to delete the successor - update the tree structure
44            root.right = self.deleteNode(root.right, successor.val)
45
46        return root
47
48        