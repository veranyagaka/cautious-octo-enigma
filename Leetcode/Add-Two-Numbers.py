1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        """
9        brute force O(n)
10        get the values -> reverse -> add -> form a linked list
11        """
12        list1, list2 = [], []
13        curr = l1
14        while curr:
15            list1.append(curr.val)
16            curr = curr.next
17
18        curr = l2
19        while curr:
20            list2.append(curr.val)
21            curr = curr.next
22
23        ## reverse
24        list1 = list1[::-1]
25        list2 = list2[::-1]
26
27        ## add
28        #sum_1 =  "".join(list1)
29        print(list1)
30        print(list2)
31        list1 = int("".join(str(x) for x in list1))
32        list2 = int("".join(str(x) for x in list2))
33
34        sum_val = list1 + list2
35        #sum_val = [x + y for x, y in zip(list1, list2)]
36        print(sum_val) # 807
37
38        # rev_sum_val = [x for x in sum_val][::-1] # 708
39        # print(rev_sum_val)
40        """
41        iterate through 807 in reverse
42        make a linkedlist
43        """
44
45        # 807
46        n = len(str(sum_val))
47        print(n)
48        list_sum_val = [int(x) for x in str(sum_val)]
49
50        dummy = ListNode()
51        curr = dummy
52
53        for i in range(n-1, -1, -1):
54            num = list_sum_val[i]
55            curr.next = ListNode(num)
56            curr = curr.next
57            # print(node.val)
58
59        return dummy.next