from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

countVec = CountVectorizer(max_features=10000, stop_words='english')
file = open('./data/movies.json', 'r', encoding='UTF-8')
data = json.load(file)
words = [movie['overview'] for movie in data]
# print(words)

dataVectors = countVec.fit_transform(words).toarray()
similarity = cosine_similarity(dataVectors)

ids = [10138, 99861, 284052]
idx = []
cnt = len(ids)
for j in range(2000):
    if data[j]['id'] in ids:
        idx.append(j)
        cnt -= 1
    if not cnt:
        break

# print(idx)
idx_collection = []
for i in idx:
    distances = similarity[i]
    listofMovies = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:7]
    idx_collection.extend(listofMovies)

pk_collection = []
for idx in idx_collection:
    if data[idx[0]]['vote_count'] >= 300 and data[idx[0]]['vote_average'] >= 5:
        pk_collection.append((data[idx[0]]['title'], idx[1]))
pk_collection.sort(key=lambda x: -x[1])
print(pk_collection)