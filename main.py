import heapq

n, m = map(int, input().split())
times = list(map(int, input().split()))


threads = [(0, i) for i in range(n)]

for i in range(m):

    job_time = times[i]

    start_time, thread_id = heapq.heappop(threads)

    print(thread_id, start_time)

    start_time += job_time

    heapq.heappush(threads, (start_time, thread_id))
