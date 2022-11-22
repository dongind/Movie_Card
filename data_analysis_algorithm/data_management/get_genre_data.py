from pprint import pprint
import requests
import json

# Setting Params
paramDict = {}
# 하기의 setdefault값 중 api_key에 본인의 api_key값을 입력
paramDict.setdefault('api_key', '39748706223d0bc28b79151440a205fc')
paramDict.setdefault('language', 'en-US')

# Request
requestData = requests.get('https://api.themoviedb.org/3/genre/movie/list', params=paramDict)
jsonData = requestData.json()

# 하기의 file_path 에 저장하고자 하는 데이터 명을 작성
file_path = "./data/genres.json"

# data리스트 정보를 file_path의 위치/이름으로 json 형태로 저장
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(jsonData['genres'], file, indent="\t", ensure_ascii = False)

