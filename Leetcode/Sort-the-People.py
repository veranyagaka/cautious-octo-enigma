1class Solution:
2    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
3        ## efficient sort
4        
5        together = list(zip(heights, names))
6
7        together = sorted(together, reverse=True)
8        return [name for _, name in together]