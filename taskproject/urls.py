# プロジェクト用ルーティング定義ファイル

from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # トップページにアクセスされたときに、taskapp/urls.pyでお願い！
    path('', include('taskapp.urls')),
]
