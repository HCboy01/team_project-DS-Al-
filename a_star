import indexing_station
import data_structure
import math

def heuristic(current, goal):
    # 맨해튼 거리 계산 (단순화된 버전, 실제 지하철 거리 데이터 필요)
    return abs(ord(current[0]) - ord(goal[0])) + abs(int(current[1:]) - int(goal[1:]))

def find_path(start, end):
    station_ls = indexing_station.station_ls()
    path = {start: [[start], 0]}
    g_cost = {start: 0}  # 비용
    f_cost = {start: heuristic(start, end)}  # g_cost + heuristic

    a_star_queue = data_structure.SortingDeQue()
    a_star_queue.append([start, f_cost[start]])
    
    while a_star_queue:
        cur_st = a_star_queue.popleft()[0]
        cur_path, cur_time = path[cur_st]

        if cur_st == end:
            return cur_path, cur_time

        for line in station_ls[cur_st]:
            for next_st in line:
                tentative_g_cost = g_cost[cur_st] + 2
                if cur_st in indexing_station.hwanseung:
                    tentative_g_cost += 3

                if next_st not in g_cost or tentative_g_cost < g_cost[next_st]:
                    g_cost[next_st] = tentative_g_cost
                    f_cost[next_st] = tentative_g_cost + heuristic(next_st, end)
                    path[next_st] = [cur_path + [next_st], g_cost[next_st]]
                    a_star_queue.append([next_st, f_cost[next_st]])
    
    return None, float('inf')
