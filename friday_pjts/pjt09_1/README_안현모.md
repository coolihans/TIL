# pjt 09 관통프로젝트

## 작성

1.  팔로우, 좋아요 

- Ajax 통신을 이용하여 팔로우 버튼과 좋아요 버튼을 구현

- 서버에서 Json 데이터를 받아와 html 을 구성

  - id 부여

  - queryselect

  - followForm 내에 eventlistener, axios, then, catch 작성

  - ```python
        followForm.addEventListener('submit', function (event) {
          event.preventDefault()
          axios({
            method: 'post',
            url: requestUrl,
            headers: {
              'x-csrftoken': csrfToken
            }
          })
            .then(res => {
              if (res.data.isFollow) {followBtn.innerText = '언팔로우'}
              else {followBtn.innerText = '팔로우'}
              followingText.innerText = res.data.followingCount
              followerText.innerText = res.data.followerCount
            })
            .catch(err => console.error(err))
        })
    ```

2. Infinite Scroll 

- index.html 구성

  ```python
  document.addEventListener('scroll', function (event) {
      const { scrollTop, clientHeight, scrollHeight } = document.documentElement
      
      if (scrollTop + clientHeight >= scrollHeight - 7) {
        axios({
          ...
        })
          .then(res => {
            const movies = res.data
            movies.forEach(movie =>{  
              ...
              ...
              ...
              MovieDiv.append(h2, p, a, hr)
  
              movieList.appendChild(MovieDiv)
            })
  
            page++
          })
          .catch(res => console.error(err))
      }
    })
  ```

- restframework, bootstrap5 



## 후기

- 공부를 제대로 했었다면 좀 더 도움이 되었을텐데... 여지껏 관통 중 가장 도움이 안되었다ㅎㅎ
- axios를 이용해 json 데이터를 받아오는 이 부분 복습을 다시 해야겠다.
- 기본적인 기능을 구현한 후에도 부트스트랩을 적용하거나 styling을 하는 부분도 중요하다..