1class Solution:
2    def commonChars(self, words: List[str]) -> List[str]:
3        from collections import Counter
4        
5        answer = Counter(words[0])
6        for word in words[1:]:
7            answer = answer & Counter(word)
8        print(answer)
9        return list(answer.elements())
10
11            
12        