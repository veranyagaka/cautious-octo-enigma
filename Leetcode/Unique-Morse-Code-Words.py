1class Solution:
2    def uniqueMorseRepresentations(self, words: List[str]) -> int:
3        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
4        morse_set = set()
5        for word in words:
6            arr = []
7            for ch in word:
8                index = ord(ch) - ord('a')
9                arr.append(morse[index])
10
11            morse_set.add("".join(arr))
12
13
14        return len(morse_set)