def mutate_string(string, position, character):
    # chars = string.split().copy()
    chars = list(string)
    chars[position] = character
    return "".join(chars)
