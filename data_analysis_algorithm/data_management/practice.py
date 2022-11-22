import json

file = open('./data/genres.json', 'r', encoding='UTF-8')
genres = json.load(file)
print(len(genres))