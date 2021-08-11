from django.contrib import admin
# .は同じディレクトリ、つまり、同じディレクトリのmodels.pyから全て読み込む
from .models import *

# adminのサイトにTaskモデルを登録する
admin.site.register(Task)