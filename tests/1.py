def areAlmostEqual(s1: str, s2: str) -> bool:
    non_equal = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            non_equal += 1
    print(non_equal)
    if non_equal == 0 or non_equal == 1:
        return True

    return False


print(areAlmostEqual("kelb", "kelb"))
