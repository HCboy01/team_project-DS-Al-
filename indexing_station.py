def station_ls() :
    station_ls = {1 : ["종로3가", 2],
            2 : ["종각", 1, 3],
            3 : ["시청", 2, 4, 6],
            4 : ["서울역", 3, 5],
            5 : ["남영", 4],
            6 : ["을지로입구", 7, 3],
            7 : ["을지로3가", 6, 8],
            8 : ["을지로4가", 7, 9],
            9 : ["동대문역사문화공원", 8, 10],
            10 : ["신당", 9]}
    return (station_ls)

def indexing(station, station_ls) :
    for i in range(len(station_ls)) :
        if station_ls[i + 1][0] == station :
            return (i + 1)