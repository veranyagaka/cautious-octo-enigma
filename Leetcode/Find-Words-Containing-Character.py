1class Solution:
2    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
3        res = []
4        for i, word in enumerate(words):
5            if x in word:
6                res.append(i)
7
8        return res