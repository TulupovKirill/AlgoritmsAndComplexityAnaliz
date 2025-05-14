import time
import random
import matplotlib.pyplot as plt
from typing import List, Dict, Set
def generate_test_case(n_items: int, conflict_prob: float) -> Dict[int, Set[int]]:
    conflicts = {i: set() for i in range(n_items)}
    for i in range(n_items):
        for j in range(i+1, n_items):
            if random.random() < conflict_prob:
                conflicts[i].add(j)
                conflicts[j].add(i)
    return conflicts
def pack_items(conflicts: Dict[int, Set[int]]) -> Dict[int, List[int]]:
    containers = {}
    item_to_container = {}
    sorted_items = sorted(conflicts.keys(), 
                         key=lambda x: len(conflicts[x]), 
                         reverse=True)
    for item in sorted_items:
        container_found = None
        for container in containers:
            can_pack = True
            for packed_item in containers[container]:
                if packed_item in conflicts[item]:
                    can_pack = False
                    break
            if can_pack:
                container_found = container
                break
        if container_found is not None:
            containers[container_found].append(item)
        else:
            new_container = len(containers)
            containers[new_container] = [item]
        item_to_container[item] = container_found if container_found is not None else new_container
    return containers
def measure_performance(n_items_range, conflict_prob=0.1, repeats=5):
    results = []
    for n_items in n_items_range:
        total_time = 0
        for _ in range(repeats):
            conflicts = generate_test_case(n_items, conflict_prob)
            start = time.perf_counter()
            pack_items(conflicts)
            end = time.perf_counter()
            total_time += end - start
        avg_time = total_time / repeats
        results.append((n_items, avg_time))
        # print(f"Items: {n_items:4d}, Time: {avg_time:.6f} sec")
    return results
def plot_results(results, conflict_prob):
    x = [r[0] for r in results]
    y = [r[1] for r in results]
    plt.plot(x, y, 'o-', label=f'Conflict probability = {conflict_prob}')
    plt.xlabel('Number of Items')
    plt.ylabel('Average Time (sec)')
    plt.title('Container Packing Algorithm Performance')
    plt.legend()
    plt.savefig("Lab9/time2.jpg")
n_items_range = range(10, 501, 20)
for prob in [0.1, 0.3, 0.5, 0.7, 0.9]:
    results = measure_performance(n_items_range, prob)
    plot_results(results, prob)