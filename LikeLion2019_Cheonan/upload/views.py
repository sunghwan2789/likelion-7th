from django.shortcuts import render, redirect, get_object_or_404
from urllib.request import urlopen
from django.http import HttpResponse, HttpResponseForbidden
from .models import Post, Like
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
import os.path
import uuid


def main(request):
    posts = Post.objects
    weather = request.GET.get('weather', '')
    # weather=''
    if weather:
        posts = posts.filter(weather=weather)
    return render(request, 'main.html', {
        'ootds': posts.order_by('-id'),
        'user': request.user,
        'weather': weather,
    })


def ootd(request):
    if not request.user.is_authenticated:
        return redirect('main')

    if request.method == "POST" and request.FILES.get('photo', '') != '':
        fs = FileSystemStorage()
        photo = request.FILES['photo']
        filename = uuid.uuid4().hex + os.path.splitext(photo.name)[1]
        while fs.exists(filename):
            filename = uuid.uuid4().hex + os.path.splitext(photo.name)[1]
        filename = fs.save(filename, photo)
        
        post = Post()
        post.user = request.user
        post.photo = filename
        post.region = request.POST['region']
        post.weather = request.POST['weather']
        post.temperature = request.POST['temperature']
        post.date = timezone.now()
        post.body = request.POST.get('body', '')
        post.save()
        return redirect('main')

    return render(request, 'ootd.html')


def like(request, post_id):
    # 손님은 좋아요 불가
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    # 좋아요 표시할 글 찾기
    post = get_object_or_404(Post, pk=post_id)
    # 이미 좋아요 표시했는지 확인
    obj = Like.objects.filter(post=post, user=request.user)
    # 좋아요 안했으면 좋아요
    if len(obj) == 0:
        obj = Like()
        obj.post = post
        obj.user = request.user
        obj.save()
    # 좋아요 했으면 좋아요 취소
    else:
        obj[0].delete()
    return redirect('main')

def weather(request, x, y):
    return HttpResponse(urlopen('http://www.kma.go.kr/wid/queryDFS.jsp?gridx=%sgridy=%s' % (x, y)).read())