# 관통프로젝트 06
## 구현 과정의 어려움
### CRUD
1. decorate의 사용 
- @require_safe => GET 
- @require_POST => POST
2. forms.py
- widget 과 forms 의 field 사용에서 어려움에 부딪혔다.
```python
release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ),
        
    )
```
- forms.DateInput() 를 했으나 type 이 문자열로 받아져서 적용이 안되는 문제가 가장 시간이 오래 걸렸다.
- attrs 를 사용해 type 을 date 로 바꿔 달력표시를 나타내게 해결했다.
- class Meta 에서 fields = '__all__' 을 이용했더니 다 적용이 되더라.
- Meta 안에다가 widgets 쑤셔 넣는 것은 권장하지 않는다고 한다.

3. views.py
- form 을 통해 유효성 검사
- 404 error 관리..
  
4. bootstrap
- 전에 배웠던 bootstrap 을 이용
- button 의 생성
- 카드 사용
- d-inline, a tag, bootsrap_form, margin 조절 등의 복습(검색)을 했다.
  
5. 이미지 첨부
- 이미지 첨부의 방법은 사용하지 않았다
- poster url 을 받아서 구현했는데 이미지 첨부의 형태로도 가능해 보인다.