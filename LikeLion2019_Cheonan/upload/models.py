from django.db import models
from django.conf import settings


class Post(models.Model):

    # 날씨 관련 상수
    맑음 = '맑음'
    비 = '비'
    눈 = '눈'
    흐림 = '흐림'
    WEATHERS = (
        (맑음, '맑음'),
        (비, '비'),
        (눈, '눈'),
        (흐림, '흐림'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자'
    )
    photo = models.ImageField(
        verbose_name='사진',
        # media 폴더 내 'images'라는 폴더에 사진들을 저장하겠다. ()
        #upload_to="images/", blank=True,
    )
    region = models.CharField(
        max_length=40,
        verbose_name='지역'
    )
    weather = models.CharField(
        max_length=6,
        choices=WEATHERS,
        verbose_name='날씨'
    )
    temperature = models.IntegerField(
        verbose_name='온도'
    )
    date = models.DateTimeField(
        verbose_name='날짜'
    )
    body = models.TextField(
        verbose_name='본문'
    )

    def likes(self):
        return Like.objects.filter(post=self)

    def comments(self):
        return Comment.objects.filter(post=self)
    
    def regionShort(self):
        arr = self.region.split(' ')
        if len(arr) == 0:
            return '대한민국'
        elif arr[0][-1] == '도':
            return arr[1]
        else:
            return arr[0]


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='게시글'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='댓글 작성자'
    )
    date = models.DateTimeField(
        verbose_name='날짜'
    )
    body = models.TextField(
        verbose_name='본문'
    )


class Like(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='게시글'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='좋아요 누른 사람'
    )

