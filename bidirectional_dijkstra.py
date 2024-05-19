import indexing_station
import heapq

def bidirectional_dijkstra(start, end):
    station_ls = indexing_station.station_ls()
    
    # Initialize forward and backward search
    forward_heap = [(0, start, [start])]  # (time, current station, path)
    backward_heap = [(0, end, [end])]  # (time, current station, path)
    forward_visited = {}
    backward_visited = {}
    
    forward_paths = {start: [start]}
    backward_paths = {end: [end]}

    while forward_heap and backward_heap:
        # Forward search step
        if forward_heap:
            f_cur_time, f_cur_st, f_cur_path = heapq.heappop(forward_heap)
            if f_cur_st in forward_visited:
                continue
            forward_visited[f_cur_st] = f_cur_time
            forward_paths[f_cur_st] = f_cur_path

            if f_cur_st in backward_visited:
                # Meeting point found
                total_time = f_cur_time + backward_visited[f_cur_st]
                path = f_cur_path + backward_paths[f_cur_st][::-1][1:]
                return path, total_time

            for line in station_ls[f_cur_st]:
                for next_st in line:
                    next_time = f_cur_time + 2
                    if f_cur_st in indexing_station.hwanseung:
                        next_time += 3
                    if next_st not in forward_visited or next_time < forward_visited[next_st]:
                        heapq.heappush(forward_heap, (next_time, next_st, f_cur_path + [next_st]))
        
        # Backward search step
        if backward_heap:
            b_cur_time, b_cur_st, b_cur_path = heapq.heappop(backward_heap)
            if b_cur_st in backward_visited:
                continue
            backward_visited[b_cur_st] = b_cur_time
            backward_paths[b_cur_st] = b_cur_path

            if b_cur_st in forward_visited:
                # Meeting point found
                total_time = b_cur_time + forward_visited[b_cur_st]
                path = forward_paths[b_cur_st] + b_cur_path[::-1][1:]
                return path, total_time

            for line in station_ls[b_cur_st]:
                for next_st in line:
                    next_time = b_cur_time + 2
                    if b_cur_st in indexing_station.hwanseung:
                        next_time += 3
                    if next_st not in backward_visited or next_time < backward_visited[next_st]:
                        heapq.heappush(backward_heap, (next_time, next_st, b_cur_path + [next_st]))

    return None, float('inf')
