from django.shortcuts import render

# Create your views here.
# CRUD : CREATE, READ, UPDATE, DELETE

# LIST 페이지 만들기

# 클래스 뷰, 함수형 뷰 2가지가 존재한다.

# 내멋대로 이것저것 하고 싶을 때, 함수형 뷰
# 장고에 기본적으로 만들어 진 것을 클래스형 뷰

# 북마크를 사용할 때, 클래스형 뷰를 사용할 예정이다.
# 웹 페이지에 접속한다. > 페이지를 본다.
# URL을 입력 > 웹 서버가 뷰를 찾아서 동작시킨다. > 응답
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url'] # 필드명 정확하게 적어준다.
    success_url = reverse_lazy('list') # 값을 입력받아서 성공하였으면, list url 로 간다.
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')




