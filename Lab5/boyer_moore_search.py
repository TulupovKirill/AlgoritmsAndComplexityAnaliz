def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    # Создание таблицы смещений
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    
    positions = []
    s = 0  # смещение

    while s <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            positions.append(s)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    
    return positions
