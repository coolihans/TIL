# PJT03 220211

## 요약
1. 전체적인 숙련도 부족..
  - class 마다의 정확한 이해를 바탕으로 사용해 봐야한다.
  - container, row, grid 등 구역 설정을 잘해 놓는 것이 아주 중요하다..
  - 사용 할 수 있는 도구를 찾지 못해 사용하는 일이 없도록 해야한다. 더 잘찾도록..
2. 반복
  - 확실히 첫 번째 구현 할 때보다 익숙해지는 것이 느껴진다.
  - 반복하면 할 수록 더 늘 수 있는 거라는 기분...기분만 가져간다.

## A. 01_nav_footer
1. 네비게이션 바 햄버거
- 네비게이션 바에서 토글이 사라져 버리는 경우가 생김.
2. 로고 이미지 삽입
- 로고 이미지와 햄버거 토글이 겹칠경우 더 안줄어들도록 해야되는 것 같은데 해결못함..
3. Login항목은 모달 컴포넌트를 통해 내부에 배치된 form 요소를 보여줌.
- 모달 컴포넌트를 쓰긴 했으나 딱히 이해한 것 같진 않음.
4. footer 와 네비게이션 바
- 두 번째 시도였으나 두 번째도 수월하지는 못했다. 하지만 저번보다는 속도가 현저히..빨라진 것은 사실이라 반복하면 될듯?
  
## B. 02_home
1. Header
- image를 불러와 집어 넣는 것 밖에 한 것이 없다.
- Carousel 컴포넌트를 사용했는데 안의 id 만 조심하면 쉽게 사용 가능한 것 같다.
2. Section
- 카드 컴포넌트를 사용하여 구성했는데 class 설정을 잘하고 grid로 계산 잘해서 구성하면 반응형으로 잘 만들 수 있었다.
```html
<!-- 카드 1 -->
      <article class="col-sm-6 col-lg-4 col-xl-3 my-1">
        <div class="card">
          <img src="images/movie1.jpg" class="card-img-top" alt="Movie Card 1">
          <div class="card-body">
            <h5 class="card-title">Shawshank Redemption</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
          </div>
        </div>
      </article>
```
## C. 03_community
1. sidebar
- List Group 컴포넌트를 사용함.
- container, row, main 등의 class 설정을 정확히 해야 헷갈리지 않고 반응형 웹을 제대로 구현할 수 있다..

2. Table
- Table 컴포넌트 활용.
'''html
 <section class="d-none d-lg-block col-lg-10">
 ```
 > lg 이상에서만 보이고 그외에는 숨는 것
 - Display 를 활용하는 것이 가장 편한 것 같다.

 3. pagination
 - 가져다 썼다..