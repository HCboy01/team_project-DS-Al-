import time
import bfs
import dijkstra

def main() :
    start, end = "도봉", "미아"
    start_time = time.time()
    print("BFS Path:", bfs.find_path(start, end))
    end_time = time.time()
    print(f"BFS time: {end_time-start_time}")
    start_time = time.time()
    print("Dijkstra Path:", dijkstra.find_path(start, end))
    end_time = time.time()
    print(f"a_star time: {end_time-start_time}")
    start_time = time.time()
    print("a_star Path:", a_star.find_path(start, end))
    end_time = time.time()
    print(f"a_star time: {end_time-start_time}")


main()
