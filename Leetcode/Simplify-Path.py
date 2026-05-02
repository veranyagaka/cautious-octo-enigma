1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        stack = []
4        print(path.split("/"))
5
6        for part in path.split("/"):
7            if part == "" or part == ".":
8                continue
9
10            elif part == "..":
11                if stack:
12                    stack.pop()
13
14            else:
15                stack.append(part)
16
17        return "/" + "/".join(stack)