from collections import Counter
from typing import List


def commonChars(words: List[str]) -> List[str]:
    answer = Counter(words[0])
    for word in words[1:]:
        answer = answer & Counter(word)
    print(answer)
    return list(answer.elements())


print(commonChars(["bella", "label", "roller"]))
