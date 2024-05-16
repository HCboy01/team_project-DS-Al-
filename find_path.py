import indexing_station
from collections import deque # 이건 구현해야하긴함 일단 임포트

def find_path(start, end) :
    station_ls = indexing_station.station_ls()
    path = {start : [[start], 0]}

    BFS_ls = deque()
    BFS_ls.append(start)
    while (True) :
        cur_st = BFS_ls.popleft() # 현재 역
        cur_path = path[cur_st][0] # 현재 역까지 온 경로

        if cur_st == end :
            return(cur_path)
        
        time = path[cur_st][1]
        for i in range(len(station_ls[cur_st])) : # 다음역 찾기
            if (i != 0) : # 환승 일때 시간만 2분 추가
                time += 2
            for j in range(len(station_ls[cur_st][i])) : # 해당 호선의 다음 역에 대해서
                next_st = station_ls[cur_st][i][j] # 다음 역 선택
                if next_st in path : # 이미 간적이 있으면
                    if time + 2 < path[next_st][1] : # 시간 비교해서 더 적은거 선택
                        BFS_ls.append(next_st) # 지금이 더 적으면 스택에 추가
                        next_path = cur_path + [next_st] # path에 경로 추가
                        path[next_st] = [next_path, time + 2]
                else : # 없으면 그냥 추가
                    BFS_ls.append(next_st)
                    next_path = cur_path + [next_st]
                    path[next_st] = [next_path, time + 2]
            time -= 2



        



#start, end = map(int, input().split())
start, end = "양주", "홍대입구"
print(find_path(start, end))