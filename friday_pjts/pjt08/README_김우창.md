# PJT08

## 2022.04.22 김우창

### 목표

- DRF(Django Rest Framework)를 활용한 API Server 제작
- Database 1:N, M:N에 대한 이해



A.  Actor
i.     배우 데이터 조회
B.  Movie
i.     영화 데이터 조회
C.  Review
i.     리뷰 데이터 조회 / 생성 / 수정 / 삭제



### 1. Model

- Movie와 Actor를 M:N 관계 (manytomanyfield)로 설정
- Revie는 Movie를 Foreignkey로 받아서 설정
- Movie, Actor, Review 관계를 설정해 줌



### 2. Serializers

- (ActorlistSerializer, ActorSerializer, MovielistSerializer, MovieSerializer,             ReviewlistSerializer, ReviewSerializer) 각각 설정
- Actor는 Movielist를 , Movie는 Actorlist, Reviewlist를 , Review는 Movie를 각각 클래스 밑에 하위 클래스로 설정
- 예시 사진에 맡게 각각의 fields를 대입해줌



### 3. Views

- review_detail, create_review를 제외한 나머지는 모두 get을 api_view로 받아서 사용함
- list는 get_list_or_404로, 아닌 애들은 get_object_or_404로
- review_detail은 update, delete 까지 내부에 함께 설정
- if/elif 문으로 GET/PUT/DELETE 각각에 맞게 이어줌



## PJT를 마치며.

- 혼자서 무작정 강의, 실습 때 따라할 때는 이해가 잘 안 된 부분이 많았는데, 페어들과 함께 PDF 순서대로 하나하나 실행해보고 오류를 찾아가면서 수정하였고, 좀 더 이해할 수 있는 계기가 되었습니다.
- postman 을 사용하여 기존의 데이터에서 수정, 삭제 등을 직접 실행해볼 수 있었습니다.
- 이번 프로젝트 때 직접 코드를 짜보고 만들어봄으로써, 다음 주 있을 월말평가에 큰 도움이 될 것 같습니다.

