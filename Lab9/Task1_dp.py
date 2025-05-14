import time
import random
import matplotlib.pyplot as plt
from typing import List, Set
def generate_test_case(n_jobs: int, n_machines: int, max_machines_per_job: int) -> List[Set[str]]:
    S = [f's{i}' for i in range(n_machines)]
    V = []
    for _ in range(n_jobs):
        k = random.randint(1, max_machines_per_job)
        machines = set(random.sample(S, k))
        V.append(machines)
    return V, set(S)
def schedule_jobs(V: List[Set[str]], S: Set[str]) -> List[List[Set[str]]]:
    remaining_jobs = V.copy()
    time_slots = []
    while remaining_jobs:
        busy_machines = set()
        current_slot = []
        i = 0
        while i < len(remaining_jobs):
            job = remaining_jobs[i]
            if not job & busy_machines:
                current_slot.append(job)
                busy_machines.update(job)
                remaining_jobs.pop(i)
            else:
                i += 1        
        time_slots.append(current_slot)
    return time_slots
def measure_performance(n_jobs_range, n_machines, max_mach_per_job=3, repeats=5):
    results = []   
    for n_jobs in n_jobs_range:
        total_time = 0
        for _ in range(repeats):
            V, S = generate_test_case(n_jobs, n_machines, max_mach_per_job)    
            start = time.perf_counter()
            schedule_jobs(V, S)
            end = time.perf_counter()
            total_time += end - start
        avg_time = total_time / repeats
        results.append((n_jobs, avg_time))
        print(f"Jobs: {n_jobs:4d}, Machines: {n_machines}, Time: {avg_time:.6f} sec")   
    return results
def plot_results(results, n_machines):
    x = [r[0] for r in results]
    y = [r[1] for r in results]
    plt.plot(x, y, 'o-', label=f'Machines = {n_machines}')
    plt.xlabel('Number of Jobs')
    plt.ylabel('Average Time (sec)')
    plt.title('Algorithm Performance Analysis')
    plt.legend()
    plt.savefig('Lab9/time.jpg')
n_jobs_range = range(100, 2001, 100)
n_machines = 20
max_mach_per_job = 3
for n_machines in [10, 20, 50]:
    results = measure_performance(n_jobs_range, n_machines, max_mach_per_job)
    plot_results(results, n_machines)