# Model Relationship 1

## Foreign Key

![image-20220413211118755](django_Model_Relationship_1.assets/image-20220413211118755.png)

![image-20220413211131848](django_Model_Relationship_1.assets/image-20220413211131848.png)

- A Many-to-one relationship
- 2개의 인자가 반드시 필요
  - 참조하는 model class  ex(Article)

- migrate 하게 되면 필드이름 + '_id' 가 추가 되어 데이터베이스 열 이름을 만듦



```python
from django.db import models
from django.conf import settings

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

![image-20220413211512348](django_Model_Relationship_1.assets/image-20220413211512348.png)



## admin site 에서 댓글 확인하는 법

![image-20220413211710847](django_Model_Relationship_1.assets/image-20220413211710847.png)



## 참조 / 역참조 in 1 : N 관계

 ![image-20220413211813999](django_Model_Relationship_1.assets/image-20220413211813999.png)

![image-20220413211923013](django_Model_Relationship_1.assets/image-20220413211923013.png)

![image-20220413212014439](django_Model_Relationship_1.assets/image-20220413212014439.png)



## Comment Create

```python
from .models import Article, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
```

### detail 페이지에서 출력

```python
# articles/views.py
from .forms import ArticleForm, CommentForm

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    # 조회한 article의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

![image-20220413234234210](django_Model_Relationship_1.assets/image-20220413234234210.png)

### 댓글 작성 로직

![image-20220413234450065](django_Model_Relationship_1.assets/image-20220413234450065.png)

![image-20220413234459079](django_Model_Relationship_1.assets/image-20220413234459079.png)

- 여기서 save(commit=False) 로 댓글 객체 저장 후 누락되었던 article 을 할당해준 후 다시 저장

- 너 이글 몇 번 글에 쓸거야? == 외래 키 article_id 가 지금 없잖아

- 기본 commit = True 

  

![image-20220413234842064](django_Model_Relationship_1.assets/image-20220413234842064.png)





## Comment Read

```python
# articles/views.py

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    # 조회한 article의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```



```python
# articles/detail.html
<h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.user }} - {{ comment.content }}
        {% if request.user == comment.user %}
          <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method = "POST">
            {% csrf_token %}
            <input type="submit" value="삭제">
          </form>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
```



## Comment Delete

![image-20220413235556395](django_Model_Relationship_1.assets/image-20220413235556395.png)

![image-20220413235751544](django_Model_Relationship_1.assets/image-20220413235751544.png)