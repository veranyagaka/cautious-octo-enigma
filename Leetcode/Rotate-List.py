1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        ## edge cases
9        if head is None or k == 0:
10            return head
11
12        n = 0
13        curr = head
14        while curr:
15            n += 1
16            curr = curr.next
17
18        k = k % n ## wrapping
19        if k%n == 0:
20            return head
21        ## print(k)
22        ## make it a cycle
23
24        for _ in range(k):
25                
26            curr = head # first element
27            prev = None
28            while curr.next:
29                prev = curr
30                curr = curr.next
31                
32            curr.next = head # connecting 5 to 1
33            head = curr
34
35            ## new tail
36            prev.next = None
37
38        return head