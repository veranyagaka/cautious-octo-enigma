1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        res = []
4
5        for hour in range(12):
6            for minute in range(60):
7
8                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
9
10                    res.append(f"{hour}:{minute:02d}")
11
12        return res
13