1class Solution:
2    def restoreString(self, s: str, indices: List[int]) -> str:
3        n = len(s)
4        arr = [""] * n
5        for i, index in enumerate(indices):
6            arr[index] = s[i]  
7        
8        return "".join(arr)