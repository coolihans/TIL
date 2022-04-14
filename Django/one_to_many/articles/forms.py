from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',)
        '''
        fields의 필드들은
        1. 유효성 검사를 하겠다.
        2. HTML에 출력될 것이다.
        '''
        # exclude = ('user', )
        '''
        excludes 의 필드들은
        1. 유효성 검사 안하겠다.
        2. HTML에 출력 안하겠다.
        '''


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)