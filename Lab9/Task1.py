class Job:
    def __init__(self, name, required_machines):
        self.name = name
        self.required_machines : list[Machine] = required_machines
class Machine:
    def __init__(self, id):
        self.id = id
        self.is_busy = False
def assign_jobs_to_machines(jobs : list[Job], machines: list[Machine]):
    job_assignment = {}
    for job in jobs:
        assigned_machines = []
        for machine in job.required_machines:
            if not machines[machine].is_busy:
                assigned_machines.append(machine)
                machines[machine].is_busy = True
        if len(assigned_machines) == len(job.required_machines):
            job_assignment[job.name] = assigned_machines
        else:
            for m in assigned_machines:
                machines[m].is_busy = False  # Rollback if not all machines could be assigned
    return job_assignment

# Пример использования
machines = [Machine(i) for i in range(5)]
jobs = [Job("Job1", [0, 1]), Job("Job2", [1, 2]), Job("Job3", [2, 3]), Job("Job4", [3, 4])]

assignment = assign_jobs_to_machines(jobs, machines)
print(assignment)
