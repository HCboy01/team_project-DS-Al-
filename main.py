import time
import bfs
import dijkstra

def main() :
    '''
    start, end = "도봉", "미아"
    start_time = time.time()
    print("BFS Path:", bfs.find_path(start, end))
    end_time = time.time()
    print(f"BFS time: {end_time-start_time}")
    start_time = time.time()
    print("Dijkstra Path:", dijkstra.find_path(start, end))
    end_time = time.time()
    print(f"Dijkstra time: {end_time-start_time}")
    '''
    start = input("출발 역을 입력하세요 : ")
    end = input("도착 역을 입력하세요 : ")
    path, time = bfs.find_path(start, end)
    print("{0}역에서 {1}역까지 가장 빠르게 갈 수 있는 경로는 {2}입니다.\n 예상 소요 시간은 {3}시간 {4}분 입니다.".format(start, end, path, time // 60, time % 60))

main()