import indexing_station
from collections import deque
import heapq
import time

def bfs_path(start, end):
    station_ls = indexing_station.station_ls()
    path = {start: [[start], 0]}

    bfs_queue = deque([start])
    while bfs_queue:
        cur_st = bfs_queue.popleft()
        cur_path, cur_time = path[cur_st]

        if cur_st == end:
            return cur_path, cur_time

        for line in station_ls[cur_st]:
            for next_st in line:
                next_time = cur_time + 1
                if cur_st in indexing_station.hwanseung:
                    next_time += 4
                if next_st in path:
                    if next_time < path[next_st][1]:
                        path[next_st] = [cur_path + [next_st], next_time]
                        bfs_queue.append(next_st)
                else:
                    path[next_st] = [cur_path + [next_st], next_time]
                    bfs_queue.append(next_st)
    
    return None, float('inf')

def dijkstra_path(start, end):
    station_ls = indexing_station.station_ls()
    min_heap = [(0, start, [start])]  # (time, current station, path)
    visited = set()

    while min_heap:
        cur_time, cur_st, cur_path = heapq.heappop(min_heap)

        if cur_st in visited:
            continue

        visited.add(cur_st)
        
        if cur_st == end:
            return cur_path, cur_time

        for line in station_ls[cur_st]:
            for next_st in line:
                next_time = cur_time + 1
                if cur_st in indexing_station.hwanseung:
                    next_time += 4
                heapq.heappush(min_heap, (next_time, next_st, cur_path + [next_st]))

    return None, float('inf')

start, end = "도봉", "마천"
start_time = time.time()
print("BFS Path:", bfs_path(start, end))
end_time = time.time()
print(f"BFS time: {end_time-start_time}")
start_time = time.time()
print("Dijkstra Path:", dijkstra_path(start, end))
end_time = time.time()
print(f"Dijkstra time: {end_time-start_time}")