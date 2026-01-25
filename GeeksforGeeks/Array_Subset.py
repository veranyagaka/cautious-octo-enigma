#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        from collections import Counter
        count_a = Counter(a)
        count_b = Counter(b)

        for key, count in count_b.items():
            if count > count_a.get(key, 0):
                return False
        return True
