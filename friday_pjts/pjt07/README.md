# 일곱번째 관통프로젝트!

## 목표
> 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
> 
> Django web framework를 통한 데이터 조작
> 
> ORM에 대한 이해
> 
> Django Authentication System에 대한 이해
> 
> Database many to noe relationship에 대한 이해
> 

## 프로젝트 과정(공영경)
이번 페어 프로젝트는 driver와 nevigator로 나눠서 진행했다. 
1. pjt07 repository 생성 후 내가 먼저 driver가 되어서 진행했다.
2. 우선, project 생성 및 app 생성, settings, urls, models, forms, admin 까지  작성한 후 역할을 바꿔 진행했다.
3. 현모님께서 views와 html을 중심으로 작성해주셨다.
4. 작성하면서 놓쳤던 부분을 같이 확인했다.
5. 특히, `update`과정이랑 `logout`/`delete`부분에서 많은 어려움을 겪었다.

## 프로젝트 진행(안현모님)

- 기본적인 틀은 금방 금방 작성해 나갈 수 있었다.

- 공부가 필요한 부분 +한 번에 안 된 부분들 (aka errors)

  - Custom User/ .get_user / get_user_model()/
  - Custom forms
  - GET 과 POST 의 요청에 따른 405 에러 => html 에서 form태그 (method="POST") 로 꼭 요청을 해야 된다. 
  - comment 옆에 comment delete 버튼을 놓으려다가 남의 comment 자체가 안보이게 되었는데 if else 를 쓰고 comment의 위치를 바꿔줘서 해결
  - movie_update 에서 context 로 'form': form 만 넘겨 주었더니 에러가 났다.
    - 'movie': movie 도 넘겨주어야 하더라. 이유가 뭘까
    - movie_detail 에서도 넘겨주어서 그런거 같기도 하고... update.html 을 더 뜯어봐야 알 것 같다.
 ```python
  @login_required
  @require_http_methods(["GET", "POST"])
  def movie_update(request, movie_pk):
      movie = get_object_or_404(Movie, pk=movie_pk)
      if request.user == movie.user:
          if request.method == 'POST':
              form = MovieForm(request.POST, instance=movie)
              if form.is_valid():
                  movie = form.save()
                  return redirect('movies:movie_detail', movie.pk)
          else:
              form = MovieForm(instance=movie)     
      else:
          return redirect('movies:movie_detail', movie.pk)
      context={
          'form': form,
          'movie': movie,
      }
      return render(request, 'movies/update.html', contex
 ```

 ## 오늘의 소감(공영경)

오늘은 현모님과 처음 페어프로그래밍을 진행했는데 덕분에 정말 많이 배울 수 있었다.

사실 프로젝트를 이해하고 구현하는데 자신이 없었다.

배운 내용이 많고 잘 적응하지 못한것 같아서 걱정이 앞섰지만 다행히 큰 어려움 없이 잘 끝냈다.

특히, 작성할 때 꼼꼼하게 작성한다고 했는데 다 작성하고 보니 에러가 나서 조금 힘들었지만 같이 수정하면서 왜 그런 에러가 났는지 알 수 있었다.

## 페어 (안현모님)
- 페어 프로그래밍이 아직은 부담스럽지만 조금 적응해 나가는 것 같다.
- 아직 git 의 충돌 등에 대해서 제대로 익히질 않아 조심스럽게 작업하는 부분이 있어 이 부분에 대해 몸으로 부딪혀서 배우는 과정이 필요해 보인다.
- 그런 이유로 따로 파트를 구분 지어 나눠서 하는 페어 프로그래밍은 아직 조금 두려운 부분이 있다..
- 갈수록 길어지는 프로젝트 시간을 보면 복습을 덜하고 있다는 느낌이 든다..ㅎㅎ..
- 확실히 같이 작업을 하기 때문에 있는 장점이 있다
  - 해야 할 것의 순서를 정하는 데 도움이 된다. 혼자하게 될 때는 머리에 맞지 않게 정리가 되지 않은 로드맵을 그리며 한 번에 많은 것을 모두 해결하려고 하지만 그런 쓸데 없는 생각을 덜하고 심플한 길을 만들어서 따라가게 된다.
  - 기본적으로 놓치게 되는 작은 실수가 적어지고 길 잃는 시간이 짧아진다.
  - 같이 코드를 따라 같이 사고하기 때문에  놓친 부분이나 에러가 나는 부분에서 이를 설명하는 데 긴 시간이 걸리지 않는다. 