import json

file1 = open('./data/genres.json', 'r', encoding='UTF-8')
file2 = open('./data/movies.json', 'r', encoding='UTF-8')
file3 = open('./data/total_similarity.json', 'r', encoding='UTF-8')
genres = json.load(file1)
movies = json.load(file2)
total_similarity = json.load(file3)

ids = [476669]
idx = []
cnt = len(ids)
for j in range(2000):
    if movies[j]['id'] in ids:
        idx.append(j)
        cnt -= 1
    if not cnt:
        break

print(idx)
idx_collection = []
for i in idx:
    distances = total_similarity[i]
    listofMovies = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
    idx_collection.extend(listofMovies)

pk_collection = []
for idx in idx_collection:
    if movies[idx[0]]['vote_count'] >= 300 and movies[idx[0]]['vote_average'] >= 5:
        pk_collection.append((movies[idx[0]]['title'], idx[1]))
pk_collection.sort(key=lambda x: -x[1])
print(pk_collection)
