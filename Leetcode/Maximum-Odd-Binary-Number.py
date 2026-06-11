1class Solution:
2    def maximumOddBinaryNumber(self, s: str) -> str:
3        """ so what im supposed to do
4        count the no of 1s but 1 at the end
5        then the rest can go in the beginning
6        then zeros in the middle
7        """
8        res = ""
9
10        no_of_1s = s.count("1")
11        no_of_0s = s.count("0")
12        res += "1" * (no_of_1s - 1)
13        res += "0" * no_of_0s
14        res += "1"
15
16        # res.append("1")
17        # "".join(res)
18
19        return res
20
21