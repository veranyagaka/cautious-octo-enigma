1class Solution:
2    def lemonadeChange(self, bills: List[int]) -> bool:
3
4        """
5        [5,5,5,10,20]
6
7        """
8        fives = 0
9        tens = 0
10        twenty = 0
11
12        for bill in bills:
13            if bill == 5:
14                fives += 1
15
16            elif bill == 10:
17                tens += 1
18                if fives < 1:
19                    return False
20                fives -= 1
21
22            else:
23                twenty += 1
24
25                if tens >= 1 and fives >=1:
26                    tens -= 1
27                    fives -= 1 
28
29                elif fives >= 3:
30                    fives -= 3
31                
32                else:
33                    return False
34
35                ## in case of 20 -> 3 fives or 1 ten and 1 five
36
37        return True
38        