import find_path
import time

def main() :
    start, end = "도봉", "미아"
    start_time = time.time()
    print("BFS Path:", find_path.bfs_path(start, end))
    end_time = time.time()
    print(f"BFS time: {end_time-start_time}")
    start_time = time.time()
    print("Dijkstra Path:", find_path.dijkstra_path(start, end))
    end_time = time.time()
    print(f"Dijkstra time: {end_time-start_time}")

main()