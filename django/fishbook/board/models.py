from django.db import models

# Create your models here.
from users.models import User

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    groupno = models.IntegerField(default=0)
    orderno = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)

# groupno 컬럼 - 첫 게시글과, 그 게시글의 답글들에게 같은 groupno을 주어서 보여주기 위함
#
# orderno 컬럼 - 같은 groupno의 게시글들을 최신순으로 위로 올리기 위함
#
# depth 컬럼 - 답글들을 한 칸씩 밀려서 보이게 하기 위함
