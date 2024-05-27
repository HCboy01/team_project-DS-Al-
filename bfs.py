import indexing_station
import data_structure

def find_path(start, end):
    station_ls = indexing_station.station_ls()
    path = {start: [[start], 0]}

    bfs_queue = data_structure.SortingDeQue()
    bfs_queue.append([start, 0])
    while bfs_queue:
        cur_st = bfs_queue.popleft()[0]
        if cur_st == "종로5가"  :
            a = 0
        cur_path, cur_time = path[cur_st]

        if cur_st == end:
            return cur_path, cur_time

        for i in range(len(station_ls[cur_st])):
            hwanseung = 0
            if i != 0 :
                hwanseung = 1
            line = station_ls[cur_st][i]
            for next_st in line:
                next_time = cur_time + 2
                if hwanseung == 1:
                    next_time += 3
                if next_st in path:
                    if next_time < path[next_st][1]:
                        path[next_st] = [cur_path + [next_st], next_time]
                        bfs_queue.append([next_st, next_time])
                else:
                    path[next_st] = [cur_path + [next_st], next_time]
                    bfs_queue.append([next_st, next_time])
    
    return None, float('inf')
