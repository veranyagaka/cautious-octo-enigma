1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
8        n = 0
9        count = head
10
11        while count:
12            n += 1
13            count = count.next
14
15        ## now we have n
16        # how big should each part be
17        ## size of each part
18        s = n // k
19        extra = n % k
20
21        res = [None] * k # for the some parts being null
22        curr = head
23        for i in range(k):
24            curr_size = s + (1 if i < extra else 0)
25
26            if curr_size == 0:
27                res[i] = None
28                continue
29
30            curr_part = curr
31
32            for _ in range(curr_size-1): # move curr
33                if curr:
34                    curr = curr.next
35
36            if curr: # cut the list
37                next_part = curr.next
38                curr.next = None
39                curr = next_part
40            res[i] = curr_part
41
42
43        return res
44        ## returning an array of listnodes
45