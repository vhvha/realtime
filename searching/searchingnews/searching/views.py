from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from bs4 import BeautifulSoup
import requests

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.save()

        return redirect('result', post.pk)
    else:
        form = PostForm()

        return render(request, 'home.html', {'form': form})


def result(request, post_pk):
    URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
    query = Post.objects.get(pk=post_pk)
    word = query.word

    fullURL = URL + word
    # 해당 URL의 모든 내용이 data 안에??
    data = requests.get(fullURL).text
    soup = BeautifulSoup(data, 'html.parser')
    # class와 id가 주소 역할
    # data를 html파일로 변환한 soup에서 class가 '_sp_each_title'인 것 모두 찾아서 모아서, 전부 news_titles 변수에 넣어라
    news_titles = soup.find_all(class_='_sp_each_title')
    title_list = []
    # 리스트 한 칸에 두개 이상을 가져오려면 딕셔너리 사용

    for title in news_titles:
        title_list.append(
            {'title': title.get('title'), 'url': title.get('href')})

    return render(request, 'result.html', {'title_list': title_list, 'query': query})
