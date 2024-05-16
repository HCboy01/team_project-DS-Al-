'''
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
'''
global hwanseung
hwanseung = []
class station_map :
    line = [0 for i in range(6)]
    line[1] = "소요산 - 동두천 - 보산 - 동두천중앙 - 지행 - 덕정 - 덕계 - 양주 - 녹양 -  가능 -  의정부 - 회룡 -  망월사 - 도봉산 - 도봉 -  방학 -  창동 -  녹천 -  월계 -  성북 -  석계 -  신이문 - 외대앞 - 회기 -  청량리 - 제기동 - 신설동 - 동묘앞 - 동대문 - 종로5가 -  종로3가 -  종각 -  시청 -  서울역 - 남영 -  용산 -  노량진 - 대방 -  신길 -  영등포 - 신도림 - 구로 -  구일 -  개봉 -  오류동 - 온수 -  역곡 -  소사 -  부천 -  중동 -  송내 -  부개 -  부평 -  백운 -  동암 -  간석 -  주안 -  도화 -  제물포 - 도원 -  동인천 - 인천 -  광명 -  가산디지털단지 - 독산 -  금천구청 -  석수 -  관악 -  안양 -  명학 -  금정 -  군포 -  당정 -  의왕 -  성균관대 -  화서 -  수원 -  세류 -  병점 -  세마 -  오산대 - 오산 -  진위 -  송탄 -  서정리 - 지제 -  평택 -  성환 - 직산 - 두정 -  천안 -  봉명 -  쌍용 -  아산 -  배방 -  온양온천 -  신창 -  서동탄"
    line[2] = "시청 -  을지로입구 - 을지로3가 - 을지로4가 - 동대문역사문화공원 - 신당 -  상왕십리 -  왕십리 - 한양대 - 뚝섬 -  성수 -  건대입구 -  구의 - 강변 - 잠실나루 -  잠실 -  신천 -  종합운동장 - 삼성 -  선릉 -  역삼 -  강남 -  교대 -  서초 -  방배 -  사당 -  낙성대 - 서울대입구 - 봉천 -  신림 - 신대방 -  구로디지털단지 - 대림 -  신도림 - 문래 -  영등포구청 - 당산 -  합정 -  홍대입구 -  신촌 -  이대 -  아현 -  충정로 - 시청"
    line[3] = "대화 -  주엽 -  정발산 - 마두 -  백석 -  대곡 -  화정 -  원당 -  삼송 -  지축 -  구파발 - 연신내 - 불광 -  녹번 -  홍제 -  무악재 - 독립문 - 경복궁 - 안국 -  종로3가 -  을지로3가 - 충무로 - 동대입구 -  약수 -  금호 -  옥수 -  압구정 - 신사 -  잠원 -  고속터미널 - 교대 -  남부터미널 - 양재 -  매봉 -  도곡 -  대치 -  학여울 - 대청 -  일원 -  수서 -  가락시장 -  경찰병원 -  오금"
    line[4] = "진접 - 오남 - 별내별가람 - 당고개 - 상계 -  노원 -  창동 -  쌍문 -  수유 -  미아 -  미아삼거리 - 길음 -  성신여대입구 -  한성대입구 - 혜화 -  동대문 - 동대문역사문화공원 - 충무로 - 명동 -  회현 -  서울역 - 숙대입구 -  삼각지 - 신용산 - 이촌 -  동작 -  이수 -  사당 -  남태령 - 선바위 - 경마공원 -  대공원 - 과천 -  정부과천청사 -  인덕원 - 평촌 -  범계 -  금정 -  산본 -  수리산 - 대야미 - 반월 -  상록수 - 한대앞 - 중앙 -  고잔 -  공단 -  안산 -  신길온천 -  정왕 - 오이도"
    line[5] = "방화 -  개화산 - 김포공항 -  송정 -  마곡 -  발산 -  우장산 - 화곡 -  까치산 - 신정 -  목동 -  오목교 - 양평 -  영등포구청 - 영등포시장 - 신길 - 여의도 -  여의나루 -  마포 -  공덕 -  애오개 - 충정로 - 서대문 - 광화문 - 종로3가 -  을지로4가 - 동대문역사문화공원 - 청구 -  신금호 - 행당 -  왕십리 - 마장 -  답십리 - 장한평 - 군자 -  아차산 - 광나루 - 천호 -  강동 -  길동 -  굽은다리 -  명일 -  고덕 -  상일동 - 둔촌동 - 올림픽공원 - 방이 -  오금 -  개롱 -  거여 -  마천"

def station_ls() :
    station_ls = {}
    for j in range(5):
        cur_line = list(station_map.line[j + 1].split(" - ")) # 리스트 자르기
        cur_line = [cur_line[i].strip() for i in range(len(cur_line))] # 공백이 두칸 이상인 애들이 있어서 안잘린 친구들 추가로 잘라줌
        for i in range(len(cur_line)) : # 호선별로 순회
            if cur_line[i] not in station_ls : # 없으면 (환승역 x)
                if i == 0 : # 호선의 출발 역이면
                    if (cur_line[0] == cur_line[-1]) : # 순환 열차인지 검사해서 다르게 추가해주는거
                        station_ls[cur_line[i]] = [[cur_line[1], cur_line[-2]]]
                    else :
                        station_ls[cur_line[i]] = [[cur_line[i + 1]]]
                elif i == len(cur_line) - 1 : # 마지막 역이면               
                    if (cur_line[0] == cur_line[-1]) :
                        continue
                    station_ls[cur_line[i]] = [[cur_line[i - 1]]]
                else : # 아니면 인접리스트로 전역 다음역 추가해줌
                    station_ls[cur_line[i]] = [[cur_line[i - 1], cur_line[i + 1]]]
            else : # 딕셔너리에 있으면 (환승역이라는 의미)
                global hwanseung # 환승역 저장하는 임시 코드임당
                if cur_line[i] not in hwanseung :
                    hwanseung.append(cur_line[i])
                if i == 0 : # 전거랑 같은방식인데 append 해줌. 구조는 시청역의 경우[['종각', '서울역'], ['을지로입구', '충정로']] 처럼 될거에요
                    if (cur_line[0] == cur_line[-1]) :
                        station_ls[cur_line[i]].append([cur_line[1], cur_line[-2]])
                    else :
                        station_ls[cur_line[i]].append([cur_line[i + 1]])
                elif i == len(cur_line) - 1 :
                    if (cur_line[0] == cur_line[-1]) :
                        continue
                    station_ls[cur_line[i]].append([cur_line[i - 1]])
                else :
                    station_ls[cur_line[i]].append([cur_line[i - 1], cur_line[i + 1]])
    return(station_ls)


station_mp = station_ls()
'''print(hwanseung)
print(station_mp["양주"])
print(station_mp["시청"])
print(station_mp["진접"])'''

'''
key = list(station_mp.keys())
for i in range(len(key)) :
    print("역 : {0}, 인접 역 : {1}".format(key[i], station_mp[key[i]]))'''