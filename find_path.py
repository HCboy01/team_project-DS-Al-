import indexing_station
from collections import deque # 이건 구현해야하긴함 일단 임포트

def find_path(start, end) :
    station_ls = indexing_station.station_ls()
    cur_st = indexing_station.indexing(start, station_ls)
    end_st = indexing_station.indexing(end, station_ls)
    path = {cur_st : [[station_ls[cur_st][0]], 0]}

    BFS_ls = deque()
    BFS_ls.append(cur_st)
    while (True) :
        cur_st = BFS_ls.popleft() # 현재 역 번호
        cur_path = path[cur_st][0] # 현재 역까지 온 경로

        if cur_st == end_st :
            return(cur_path)
        
        time = path[cur_st][1]
        for i in range(len(station_ls[cur_st]) - 1) :
            next_st = station_ls[cur_st][i + 1]
            if next_st in path :
                if time + 2 < path[next_st][1] :
                    BFS_ls.append(station_ls[cur_st][i + 1])
                    next_path = cur_path + [station_ls[next_st][0]]
                    path[next_st] = [next_path, time + 2]
            else :
                BFS_ls.append(station_ls[cur_st][i + 1])
                next_path = cur_path + [station_ls[next_st][0]]
                path[next_st] = [next_path, time + 2]


        



#start, end = map(int, input().split())
start, end = "종로3가", "신당"
print(find_path(start, end))