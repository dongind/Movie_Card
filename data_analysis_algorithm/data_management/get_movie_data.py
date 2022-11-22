from pprint import pprint
import requests
import json

# Setting Params
paramDict = {}
# 하기의 setdefault값 중 api_key에 본인의 api_key값을 입력
paramDict.setdefault('api_key', '39748706223d0bc28b79151440a205fc')
paramDict.setdefault('language', 'en-US')
paramDict.setdefault('page', 0)

# 최종 데이터를 저장할 data list
data = []

# 반복 횟수를 증가할 때마다, movies.json의 데이터에 20개의 데이터가 추가적으로 생성
for i in range(1):
    paramDict['page'] += 1

    # Request
    requestData = requests.get('https://api.themoviedb.org/3/movie/popular', params=paramDict)
    jsonData = requestData.json()

    # request로 반환된 jsonData 중 result의 영화들을 data 리스트에 저장
    for movie in jsonData['results']:
        data.append(movie)

# 하기의 file_path 에 저장하고자 하는 데이터 명을 작성
file_path = "./data/genres.json"

# data리스트 정보를 file_path의 위치/이름으로 json 형태로 저장
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent="\t", ensure_ascii = False)

