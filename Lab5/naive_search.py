def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            positions.append(i)
    return positions