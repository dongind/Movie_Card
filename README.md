# MoCa (Movie Card)



### 1. 개요

---

주제 : 추천 알고리즘이 적용된 영화 커뮤니티 웹 사이트

방식 : 장르와 키워드를 통해 코사인 유사도 방식을 활용하여 가장 유사도가 높은 영화를 추천

기간 : 2022.11.15 (화) ~ 2022.11.25 (금)

발표 : 2022.11.25 (금)

기술 스택 : DRF + Vue



### 2. 팀원

---

| 이름   | 담당 영역                                                    | Github                                             |
| ------ | ------------------------------------------------------------ | -------------------------------------------------- |
| 김용현 | 프론트엔드(60%) / 백엔드(40%)<br />-  프론트엔드 기능 구현 및 디버깅, 테스트, 디자인 + 추천 알고리즘 | https://github.com/dongind                         |
| 이승호 | 프론트엔드(40%) / 백엔드(60%)<br />- 백엔드 데이터 로직 작성 및 디버깅, DB 모델링 | https://github.com/seungho-l-7946?tab=repositories |





### 3. 프로젝트 컨셉 및 주요 기능

---

1. 서비스 컨셉 및 기획 의도

```
영화 시청을 좋아하지만, 
위시리스트를 해결하지 못하고 쌓아가기만 하는 당신에게...

해당 작품에 대한 리마인드와 동시에, 자신의 의견을 공유할 수 있는 서비스를 제공합니다.
```



2. 주요 기능

| 서비스 명             | 무카 (무비 카드)                 |
| --------------------- | -------------------------------- |
| 서비스 컨셉           | 영화 다이어리 & 플래너           |
| 필수 기능             | 로그인, 회원 가입, 관리자 페이지 |
| 주 기능               | 리뷰 & 플래너 작성               |
| 부 기능 1             | 알고리즘 영화 추천               |
| 부 기능 2             | 리뷰 공유 및 프로필              |
| 부 기능 3 (고려 사항) | 마이 페이지, 좋아요              |



3. 서비스 플로우 차트

![image-20221125055200784](C:\Users\82105\Desktop\마지막\final_pjt_new\README.assets\image-20221125055200784.png)
![image-20221125055148942](https://user-images.githubusercontent.com/109324469/203861714-d13a44d5-f9fd-476b-b876-728fe383a56d.png)



4. 서비스 구현

| No.  | Name                | Content                                                      | Implementation |
| ---- | ------------------- | ------------------------------------------------------------ | -------------- |
| 1    | 로그인/아웃/        | -                                                            | ★★★★★          |
| 2    | 회원가입            | 회원가입 시, 시청한 영화를 선택하여 이를 기반으로 개인별 추천 알고리즘이 작동될 수 있도록 유도함 | ★★★★★          |
| 3    | 관리자 페이지       | 유저/게시물/DB 관리                                          | ★★★★★          |
| 4    | 카드 및 영화 리스트 | 내가 작성한 영화 리뷰나 플래너를 모아볼 수 있는 페이지와 영화들을 필터링하여 볼 수 있는 페이지를 구현 | ★★★★★          |
| 5    | 개인 맞춤 영화 추천 | 회원이 시청한 영화의 장르/키워드 데이터를 기반으로 하였으며, 또한 해당 회원이 평가했던 평점을 기반으로 가중치를 주어 DB내의 모든 영화에 대해 코사인 유사도를 계산하였음 | ★★★★★          |
| 6    | 영화 필터링         | 추천별, 인기별, 최신별, 장르별                               | ★★★★★          |
| 7    | 비슷한 영화 추천    | 코사인 유사도를 기반으로 내림차순으로 정렬하여, 해당 영화와 비슷한 영화들을 추천 | ★★★★★          |
| 8    | 영화별 리뷰 CRUD    | 시청한 영화들에 대한 후기를 작성하여 나만의 카드로 만들어서 보관이 가능 | ★★★★☆          |
| 9    | 영화별 플래너 CRUB  | 시청하고 싶은 영화들에 대한 플래너를 만들어 나만의 카드로 만들어서 보관이 가능 | ★★★★☆          |
| 10   | 타 회원 리뷰 보기   | 영화 디테일 페이지에서 해당 영화에 대해 타 회원들이 리뷰를 작성했는지 볼 수 있음 | ★★★★☆          |



### 4. DB Model (ERD)

---

![image-20221125055225847](C:\Users\82105\Desktop\마지막\final_pjt_new\README.assets\image-20221125055225847.png)



### 5. Component 구조도

---

![image-20221125055148942](C:\Users\82105\Desktop\마지막\final_pjt_new\README.assets\image-20221125055148942.png)



### 6. 웹 페이지 overview

---





### 7. 구조 Detail

---

| No.  | Issue                                 | Content                                                      | Condition |
| ---- | ------------------------------------- | ------------------------------------------------------------ | --------- |
| 1    | 알고리즘 데이터 전처리                | 단어들의 출현 수를 카운트할 수 있도록 벡터화하는 과정<br />벡터값들을 행렬로 나타낸다고 할 경우,<br />행이 각 데이터(영화; ex.토르)가 되고, 열이 각각의 특성값(장르; ex.액션)으로 대표됨<br />각 데이터별로 특성이 존재할 경우 1로, 존재하지 않을 경우 0으로 표기됨 | completed |
| 2    | 추천 알고리즘 구조화                  | 알고리즘 데이터 전처리 과정을 이용하여 장르별로, 개요 속에 존재하는 키워드 별로 영화마다 각각 벡터화한 데이터를 가져옴<br />고객들이 해당 영화에 부여한 가중치 값에 맞춰서 각 벡터값들에게 곱해줌<br />장르 유사도와 키워드 유사도를 각각 행열에 맞게 곱하여 전체 유사도 값을 만들어냄<br />전체 유사도 값을 기준으로 하여 전체 영화 리스트와 코사인 유사도 값을 계산하여 내림차순으로 정렬함<br />상위 x개의 값을 추출하여 추천 영화 리스트로 사용 | completed |
| 3    | 비슷한 영화 알고리즘 구조화           | 초기에는, 시리얼라이저나 views.py 내에서 구현하려고 했으나, model과 json파일 내에서 해결하고자 하는 방향성으로 수정<br />이후, 추천 알고리즘과 같은 방식으로 상위 5개의 리스트를 뽑아 json 파일로 만들어 similar movies 라는 새로운 model을 만들었음<br />참조 관계를 통해서 비슷한 영화 데이터를 뽑아오는 과정을 거침 | completed |
| 4    | 동일 영화에 대한 카드 중복 생성       | 하나의 영화를 시청했거나, 시청하고 싶을 때 카드를 만드는데, 동일 유저가 동일 영화에 대해서 여러개의 카드를 생성할 수 있는 이슈가 발생<br />참조관계를 잘 이용하여 back-end 의 views.py 에서 데이터를 필터링하는 과정을 거침 | completed |
| 5    | 회원가입 시, 첫 영화 선택 데이터 저장 | 초기에는, 모달을 사용하여 회원가입 시, 개인 추천 알고리즘 기반 데이터를 받고자 했으나 모달 창에서는 회원가입된 회원의 토큰이 넘어가지 않는 상황이 발생<br />따라서, 모달대신 새로운 창을 열어 회원이 개인 선호 영화를 고를 수 있는 과정을 추가 | completed |



### 8. 느낀점

---

| 이름   | 내용                                                         |
| ------ | ------------------------------------------------------------ |
| 김용현 |                                                              |
| 이승호 | 학기 동안 9회에 걸쳐 관통 프로젝트를 진행하며, 마지막 프로젝트에 대한 예행 연습을 진행해왔다고 생각했습니다. 하지만, 이정도 규모의 프로젝트를 처음했기 때문인지 프로젝트 기간의 분배를 제대로 수행해내지 못한 것 같습니다. <br />또한, 개발 과정에서 팀원과 함께 의견을 맞춰나가는 과정도 아직은 미숙한 모습이 많았다고 생각합니다. 의견을 조율해야 할 때, 서로가 사용하는 용어의 정의가 명확하지 않거나 프로세스의 구조화가 체계적이지 않을 경우 의사소통에서 착오가 생길 수 있다는 점을 깨달았습니다.<br />그리고 저 자신은 이슈관리에 대한 대처가 굉장히 미숙하다는 점까지 알 수 있었습니다. <br />전체적으로 이러한 부족한 점들도 인해 원하는 결과물을 만들지 못했다는 아쉬운 점을 남겼습니다. 하지만, 프로젝트 정규 기간이 지나고 나서 보수과정을 거쳐, 조금 더 디벨롭을 해야할 것 같다는 새로운 동기부여를 받을 수 있는 시간이었습니다. 또한, 전체적으로 프로젝트 기간을 되돌아 보며 시간관리에 대한 저만의 테크닉을 정리해야할 필요성을 느꼈습니다.<br />이렇듯, 싸피 1학기 최종 프로젝트는 미래에 진행할 제 프로젝트의 좋은 거름이 될 것 같다는 생각이 많이 들었습니다. |
