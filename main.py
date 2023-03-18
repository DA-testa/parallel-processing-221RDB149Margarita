import heapq

n, m = map(int, input().split())
times = list(map(int, input().split()))

# Initialize the heap with the starting times of each thread
threads = [(0, i) for i in range(n)]

# Process each job
for i in range(m):
    # Get the next job time from the input
    job_time = times[i]
    # Get the next available thread from the heap
    start_time, thread_id = heapq.heappop(threads)
    # Output the thread and start time for this job
    print(thread_id, start_time)
    # Update the start time for this thread
    start_time += job_time
    # Add the thread back to the heap with its updated start time
    heapq.heappush(threads, (start_time, thread_id))
