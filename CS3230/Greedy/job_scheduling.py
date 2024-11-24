# Set of jobs with deadlines and profits 
# Scheduled subset of jobs with maximum profit obtained as final output

def job_scheduling(jobs):
    # 1. Find the maximum deadline first
    max_deadline = jobs[0][1]
    for job in jobs:
        max_deadline = max(max_deadline, job[1])
    
    # 2. Sort the jobs in descending order of profits
    sorted_jobs = sorted(jobs, key=lambda a: a[2], reverse=True)
    
    print(sorted_jobs) 
    
    curr_deadline = 0
    res_jobs = []
    for _, job in enumerate(sorted_jobs):
        if curr_deadline >= max_deadline:
            break
        if (curr_deadline + job[1]) > max_deadline:
            continue
        res_jobs.append(job)
        curr_deadline += job[1]
        
    return res_jobs

# arr = [
#     ['a', 2, 100], 
#     ['b', 2, 20], 
#     ['c', 1, 40], 
#     ['d', 3, 35], 
#     ['e', 1, 25]
    # ]
arr = [
    ['a', 2, 20], 
    ['b', 2, 60], 
    ['c', 1, 40], 
    ['d', 3, 100], 
    ['e', 4, 80]
    ]

print("Scheduled Jobs: ", job_scheduling(arr))