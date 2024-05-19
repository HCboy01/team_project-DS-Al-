import indexing_station
import heapq

def find_path(start, end):
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
                next_time = cur_time + 2
                if cur_st in indexing_station.hwanseung:
                    next_time += 3
                heapq.heappush(min_heap, (next_time, next_st, cur_path + [next_st]))

    return None, float('inf')