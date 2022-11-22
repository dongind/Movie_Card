from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

file1 = open('./data/genres.json', 'r', encoding='UTF-8')
file2 = open('./data/movie_data.json', 'r', encoding='UTF-8')
genres = json.load(file1)
movies = json.load(file2)

N = len(movies) - 19

genre_idx = dict()
for i in range(19):
    genre_idx[genres[i]["id"]] = i

# 장르 유사도 계산
genre_vector = [[0 for _ in range(19)] for _ in range(N)]

# for i in range(N):
#     for genre_id in movies[i]['genre_ids']:
#         idx = genre_idx[genre_id]
#         genre_vector[i][idx] = 1

for i in range(len(movies)):
    if movies[i]['model'] == 'movies.movie':
        for genre_id in movies[i]['fields']['genres']:
            idx = genre_idx[genre_id]
            genre_vector[i - 19][idx] = 1

genre_similarity = cosine_similarity(genre_vector)

# overview_유사도 계산
count_vec = CountVectorizer(max_features=10000, stop_words='english')
# overviews = [movie['overview'] for movie in movies]
overviews = []
for movie in movies:
    if movie['model'] == 'movies.movie':
        overviews.append(movie['fields']['overview'])

# overiews 데이터를 기반으로 벡터화
overview_vectors = count_vec.fit_transform(overviews).toarray()
similarity = cosine_similarity(overview_vectors)

# 전체 유사도(장르 유사도 * overview 유사도)
total_similarity = [[0 for _ in range(N)] for _ in range(N)]
for col in range(N):
    for row in range(N):
        total_similarity[col][row] = genre_similarity[col][row] * similarity[col][row]

# # 하기의 file_path 에 저장하고자 하는 데이터 명을 작성
# file_path = "./data/total_similarity.json"

# # data리스트 정보를 file_path의 위치/이름으로 json 형태로 저장
# with open(file_path, 'w', encoding='utf-8') as file:
#     json.dump(total_similarity, file, indent="\t", ensure_ascii = False)

result = []

for x in range(len(total_similarity)):

    r2 = []

    total_list = sorted(list(enumerate(total_similarity[x])), reverse=True, key=lambda x:x[1])[1:6]

    for item in total_list:
        r2.append(item[0])

    fields = {
        "movie": x + 1,
        "similar1_idx": r2[0] + 1,
        "similar1_title": movies[r2[0] + 19]['fields']['title'],
        "similar1_poster_path": movies[r2[0] + 19]['fields']['poster_path'],
        "similar2_idx": r2[1] + 1,
        "similar2_title": movies[r2[1] + 19]['fields']['title'],
        "similar2_poster_path": movies[r2[1] + 19]['fields']['poster_path'],
        "similar3_idx": r2[2] + 1,
        "similar3_title": movies[r2[2] + 19]['fields']['title'],
        "similar3_poster_path": movies[r2[2] + 19]['fields']['poster_path'],
        "similar4_idx": r2[3] + 1,
        "similar4_title": movies[r2[3] + 19]['fields']['title'],
        "similar4_poster_path": movies[r2[3] + 19]['fields']['poster_path'],
        "similar5_idx": r2[4] + 1,
        "similar5_title": movies[r2[4] + 19]['fields']['title'],
        "similar5_poster_path": movies[r2[4] + 19]['fields']['poster_path'],
    }

    r1 = {
        "model": "movies.similar",
        "pk": x + 1,
        "fields": fields
    }

    result.append(r1)

# 하기의 file_path 에 저장하고자 하는 데이터 명을 작성
file_path = "./data/similar/similar_movies.json"

# data리스트 정보를 file_path의 위치/이름으로 json 형태로 저장
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(result, file, indent="\t", ensure_ascii = False)



# 기존코드

#     file1 = open('./data/genres.json', 'r', encoding='UTF-8')
# file2 = open('./data/movies.json', 'r', encoding='UTF-8')
# genres = json.load(file1)
# movies = json.load(file2)
# genre_idx = dict()
# for i in range(19):
#     genre_idx[genres[i]["id"]] = i

# # 장르 유사도 계산
# genre_vector = [[0 for _ in range(19)] for _ in range(2000)]

# for i in range(2000):
#     for genre_id in movies[i]['genre_ids']:
#         idx = genre_idx[genre_id]
#         genre_vector[i][idx] = 1

# genre_similarity = cosine_similarity(genre_vector)

# # overview_유사도 계산
# count_vec = CountVectorizer(max_features=10000, stop_words='english')
# overviews = [movie['overview'] for movie in movies]
# # overiews 데이터를 기반으로 벡터화
# overview_vectors = count_vec.fit_transform(overviews).toarray()
# similarity = cosine_similarity(overview_vectors)

# # 전체 유사도(장르 유사도 * overview 유사도)
# total_similarity = [[0 for _ in range(2000)] for _ in range(2000)]
# for col in range(2000):
#     for row in range(2000):
#         total_similarity[col][row] = genre_similarity[col][row] * similarity[col][row]

# # 하기의 file_path 에 저장하고자 하는 데이터 명을 작성
# file_path = "./data/total_similarity.json"

# # data리스트 정보를 file_path의 위치/이름으로 json 형태로 저장
# with open(file_path, 'w', encoding='utf-8') as file:
#     json.dump(total_similarity, file, indent="\t", ensure_ascii = False)