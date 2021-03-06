# 관통프로젝트 05. 프레임워크 기반 웹페이지 구현

## 목표

- Django web framework 사용
- 데이터를 생성, 조회, 수정, 삭제(CRUD) 할 수 있는 web application 제작

- 관리자 사이트 등록



## 과정

- 기본적인 틀을 잡는 부분이 아직 그렇게 익숙하지는 않았다.
- 가상환경 설정, pip 설치 어플등록 등등 기본적인 과정이 뚝딱거렸다..
- 확실히 이해하지 않고 외워서 치는 느낌이 있다 보니 머리에 잘 들어오지 않은 것 같다.
- 작성 흐름대로 수업 했던 그대로 내용이라 그래도 진행은 됐다!

### Models

- models.py 작성
- class Movie 를 만든 후 다양한 model field type 에 대해서 찾아보고 알맞게 넣어야 하는데 데이터 유형이 주어져서 쉽게 넘어갔다.

### urls

- 아직 안 만들어진 views 를 import 해와서 먼저 작성하는데 이름이 같아 헷갈리지는 않았다. 주어져 있기도 했고..
- 따옴표, `<int:pk>`  을 넣는 것, app_name 과 name 을 나중에 끌어다 쓸 것이다. 

###  views

- 가장 헷갈리는 부분인 것 같다.
- edit -> update 로 이어져서 redirect 로 끝나는 부분이 이해가 잘 안되어 작성할 때 머뭇거리게 된다.
- redirect 하는 view 들은 template 이 따로 필요 없다는 것을 생각했다. 



### html templates

- `url 'app_name: name'` 이 부분에서 `movie.pk` 를 까먹지 않아야 한다고 강조를 많이 해주셔서 잘 넘어갔다.
- 이미지주소를 넣는 부분에서 `"{{movie.poster_url}}"`가 작동을 제대로 해서 이상했다.
- new.html 에서 다양한 input type 외에도 정보를 입력 받을 수 있는 폼들을 찾아보면서 작성했다.
- edit.html 에서 기존 작성글을 유지시켜야되는 부분에서 text 부분은 reset 도 되고 다 됐지만 날짜를 고르는 부분이나 장르를 고르는 부분에서는 원래 선택사항을 유지시키지 못했다.



### 정리

- 기본적인 흐름대로 작성하는 데는 시간이 조금 걸려도 천천히 진행할 수 있었다.
- 페어로 진행을 하다보니 혼자하면 자신이 없거나 헷갈릴 경우에도 너무 조심하지 않고 진행을 하는 것이 가능했던 것 같다. 틀린 부분을 실시간으로 지적당하는 것이 시간을 훨씬 줄여준다. 다음 해야 할 것에 대한 생각에 오랜 시간을 고민할 필요가 적어지는 것 또한 그 이유 같았다.
- POST 로 받는 것을 하지 않고 기본 GET 으로 진행했는데 어떠한 경우에 POST 를 써야 하는지 다시 찾아봐야겠다.
- bootstrap 을 쓰지 않아 빠르고 간단하게 구현했는데 아마 적용하는 연습도 해봐야지 싶다...