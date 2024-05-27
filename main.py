import time
import bfs
import dijkstra
import a_star
import bidirectional_dijkstra

def main() :
    start, end = "도봉", "미아"
    start_time = time.time()
    print("BFS Path:", bfs.find_path(start, end))
    end_time = time.time()
    print(f"BFS time: {end_time-start_time}")
    start_time = time.time()
    print("Dijkstra Path:", dijkstra.find_path(start, end))
    end_time = time.time()
    print(f"Dijkstra time: {end_time-start_time}")
    #start_time = time.time()
    #print("a_star Path:", a_star.find_path(start, end))
    #end_time = time.time()
    #print(f"a_star time: {end_time-start_time}")
    start_time = time.time()
    print("bidirectional_dijkstra Path:", bidirectional_dijkstra.find_path(start, end))
    end_time = time.time()
    print(f"bidirectional_dijkstra time: {end_time-start_time}")
    '''
    start = input("출발 역을 입력하세요 : ")
    end = input("도착 역을 입력하세요 : ")
    path, path_time = bfs.find_path(start, end)
    print("BFS: {0}역에서 {1}역까지 가장 빠르게 갈 수 있는 경로는 {2}입니다.\n 예상 소요 시간은 {3}시간 {4}분 입니다.".format(start, end, path, path_time // 60, path_time % 60))
    path, path_time = dijkstra.find_path(start, end)
    print("Dijkstra: {0}역에서 {1}역까지 가장 빠르게 갈 수 있는 경로는 {2}입니다.\n 예상 소요 시간은 {3}시간 {4}분 입니다.".format(start, end, path, path_time // 60, path_time % 60))
    '''
# 29 * 2 + 20 = 78분 1시간 18분

# 28 * 2 56 
main()