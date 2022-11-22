from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm
import json

file1 = open('./data/genres.json', 'r', encoding='UTF-8')
file2 = open('./data/movies.json', 'r', encoding='UTF-8')
genres = json.load(file1)
movies = json.load(file2)


def cosine_similar(user_genre_vector, user_overview_vector, genre_vectors, overview_vectors):
    result = [0 for _ in range(2000)]
    for i in range(2000):
        # genre 코사인 유사도 계산
        if norm(user_genre_vector) * norm(genre_vectors[i]):
            genre_similarity = dot(user_genre_vector, genre_vectors[i]) / (norm(user_genre_vector) * norm(genre_vectors[i]))
        # overview 코사인 유사도 계산
        if norm(user_overview_vector) * norm(overview_vectors[i]):
            overview_similarity = dot(user_overview_vector, overview_vectors[i]) / (norm(user_overview_vector) * norm(overview_vectors[i]))
        # total 코사인 유사도 계산
        result[i] = genre_similarity * overview_similarity
    return result


# 0. 유저 선택 영화
ids = [438148]
rate = [3, 4, 5]
rate_fix = [1, 2, 3]
# idx : 유저 선택 영화의 index
idx = []
cnt = len(ids)
for j in range(2000):
    if movies[j]['id'] in ids:
        idx.append(j)
        cnt -= 1
    if not cnt:
        break

# 1. 유저 장르 벡터 생성
genre_idx = dict()
for i in range(19):
    genre_idx[genres[i]["id"]] = i
user_genre_vector = [0 for _ in range(19)]
genre_vectors = [[0 for _ in range(19)] for _ in range(2000)]

for i in range(2000):
    for genre_id in movies[i]['genre_ids']:
        index = genre_idx[genre_id]
        genre_vectors[i][index] = 1

for i in range(len(idx)):
    for genre_id in movies[idx[i]]['genre_ids']:
        index = genre_idx[genre_id]
        user_genre_vector[index] += (1 * rate_fix[i])


# 2. 유저 overview 벡터 생성
countVec = CountVectorizer(max_features=10000, stop_words='english')
overviews = [movie['overview'] for movie in movies]
overview_vectors = countVec.fit_transform(overviews).toarray()

user_overview_vector = [0 for _ in range(10000)]
for i in range(len(idx)):
    for j in range(10000):
        user_overview_vector[j] += overview_vectors[idx[i]][j] * rate_fix[i]
    
# 3. cosine similarity 계산
user_similarity = cosine_similar(user_genre_vector, user_overview_vector, genre_vectors, overview_vectors)

# 4. 추천 영화 추출
recommend_movie = sorted(list(enumerate(user_similarity)), reverse=True, key=lambda x:x[1])[0:6]

pk_collection = []
for idx in recommend_movie:
    if movies[idx[0]]['vote_count'] >= 300 and movies[idx[0]]['vote_average'] >= 5:
        pk_collection.append((movies[idx[0]]['title'], idx[1]))
pk_collection.sort(key=lambda x: -x[1])
print(pk_collection)
