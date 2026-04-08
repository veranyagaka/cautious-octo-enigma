1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0, head)
9        prev, curr = dummy, head
10
11        while curr and curr.next: # at least two nodes to reverse
12            # save some pointers
13            nextPair = curr.next.next
14            second = curr.next
15
16            #reverse this pair
17            second.next = curr
18            curr.next = nextPair
19            prev.next = second # making it the head now
20
21            prev = curr
22            curr = nextPair
23
24        return dummy.next
25
26        
27        """
28        neetcode help
29        dummy node
30        prev, curr,
31        swap the pointer
32        make the new head
33        next two no reverse
34        point last to null
35
36        """