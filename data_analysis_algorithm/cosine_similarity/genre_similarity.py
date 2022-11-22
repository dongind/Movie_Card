from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

file1 = open('./data/genres.json', 'r', encoding='UTF-8')
file2 = open('./data/movies.json', 'r', encoding='UTF-8')
genres = json.load(file1)
movies = json.load(file2)
genre_idx = dict()
for i in range(19):
    genre_idx[genres[i]["id"]] = i

genre_vector = [[0 for _ in range(19)] for _ in range(2000)]

for i in range(2000):
    for genre_id in movies[i]['genre_ids']:
        idx = genre_idx[genre_id]
        genre_vector[i][idx] = 1

genre_similarity = cosine_similarity(genre_vector)

ids = [10138, 99861, 284052]
idx = []
cnt = len(ids)
for j in range(2000):
    if movies[j]['id'] in ids:
        idx.append(j)
        cnt -= 1
    if not cnt:
        break

# 장르 유사도 계산
idx_collection1 = []
for i in idx:
    distances = genre_similarity[i]
    genre_movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
    idx_collection1.extend(genre_movie_list)

pk_collection = []
for idx in idx_collection1:
    if movies[idx[0]]['vote_count'] >= 300 and movies[idx[0]]['vote_average'] >= 5:
        pk_collection.append((movies[idx[0]]['title'], idx[1]))
pk_collection.sort(key=lambda x: -x[1])


