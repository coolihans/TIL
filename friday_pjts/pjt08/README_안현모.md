# pjt 08 

## 구현

1. Fixture data
   - 만들어진 데이터를 load 하는 거지 새로운 데이터를 채워 넣는 것이 아니다.
   - load 를 영어 그대로 이해하면 된다. 없는 것을 load 할 수는 없다..
   - 그래서 주어진 fixture 파일에 있는 데이터를 load 해서 써먹었다.

```python
migrate 이후

$ python manage.py loaddata movies/actiors.json ....
```

2. Models.py

   - 처음에 manytomany field 나 foreignkey 의 위치 때문에 애를 먹었다.
   - 나름 머리를 굴려 적었는데 ERD에서 table_name이 달라 고쳤는데 fixture data 를 제대로 load 하기 위해서는 원래 것이 맞았다. (pdf의 ERD 는 잘못 나온 것)

3.  admin.py

   - list_display 를 통해 index 에서 보여줄 항목을 정할 수 있었다.

   - 등록만 하면 된다.

   - ```python
     admin.site.register(Movie, MoviesAdmin)
     admin.site.register(Actor)
     admin.site.register(Review)
     ```

4. serializers.py

   - 하나의 serializer 안에 다른 serializer를 선언해주면서 커스텀해서 써먹는 건데 생각보다 잘 구현이 바로 되었다.

   - fields 의 튜플 안에는  ',' 꼭 끝에 붙이자...

   - read_only 에 대해서는 에러버깅을 하면서 해결은 했지만 이유를 다시 공부해봐야겠다.

     ```python
     class MovieSerializer(serializers.ModelSerializer):
         
         class ActorlistSerializer(serializers.ModelSerializer):
             class Meta:
                 model = Actor
                 fields = ('name',)
     
         class ReviewlistSerializer(serializers.ModelSerializer):
             class Meta:
                 model = Review
                 fields = ('title', 'content',)
     
         actors = ActorlistSerializer(many=True, read_only=True)
         review_set = ReviewlistSerializer(many=True, read_only=True)
     
         class Meta:
             model = Movie
             fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date' , 'poster_path',)
     ```

5. views.py
   - serializer 로 넘어오니까 form 에서 했던 것 보다 간결하고 쉬워서 편했다.
   - 몇 가지 사항만 주의하면 동작하는데 문제가 없었다.
   - review를 detail, update, delete 를 나눠서 정의해야 페이지에서 따로 나오는 듯해 보이지만 기능상에는 문제가 없기 떄문에 뒀다.

## 배운 점 등등

1. 앞선 관통들보다는 머리가 덜 아팠던 편이다..
2. models.py 에서 mtm , otm 등의 relationship을 고민하는게 제일 중요한 것 같다. views 코드 등은 그 뒤에 쉽게 따라오는 기분이다.
3. 오늘 최적화에 대한 수업을 했는데 아직은 감이 잘 안 잡힌다. 적은 데이터로 공부를 하다보니 아직 그 느낌이 안 오는 것 같다. 97% 는 잊어버리라니 천천히 생각해 봐야겠다.