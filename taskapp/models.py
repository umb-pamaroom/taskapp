# データベースの枠組みを作っているファイル
from django.db import models
from django.db.models.fields import CharField

# djangoでデータベースのルールを作る

# models.Modelはルール
class Task(models.Model):
    # titleは、CharFieldを使ってテキストのデータであるように指示する、最大200文字
    title=models.CharField(max_length=200)
    # デフォルトでは、Falseを入れておく
    complete=models.BooleanField(default=False)
    # createdはタスクを作成した日、auto_now_addは、データベースにデータを追加した日時
    created=models.DateTimeField(auto_now_add=True)

    # adminでタスクを追加した場合にきちんと名前を表示するために
    def __str__(self):
        return self.title
