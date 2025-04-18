def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101  # простое число для хеширования
    d = 256  # количество символов в алфавите

    h_pattern = 0  # хеш подстроки
    h_text = 0  # хеш текста
    positions = []
    h = 1

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % prime
        h_text = (d * h_text + ord(text[i])) % prime

    for i in range(n - m + 1):
        if h_pattern == h_text:
            if text[i:i + m] == pattern:
                positions.append(i)

        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % prime
            h_text = (h_text + prime) % prime  # чтобы избежать отрицательных значений

    return positions
