import time

from naive_search import naive_search
from boyer_moore_search import boyer_moore_search
from rabin_karp_search import rabin_karp_search
from kmp_search import kmp_search

def test_search_algorithms(text, pattern):
    algorithms = {
        "Naive": naive_search,
        "Boyer-Moore": boyer_moore_search,
        "Rabin-Karp": rabin_karp_search,
        "KMP": kmp_search,
    }

    for name, algorithm in algorithms.items():
        start_time = time.time()
        positions = algorithm(text, pattern)
        end_time = time.time()
        print(f"{name} found pattern at positions: {positions} in {end_time - start_time:.6f} seconds")

# Пример текста и подстроки
text = "ABABDABACDABABCABAB"
pattern = "ABAB"

test_search_algorithms(text, pattern)
