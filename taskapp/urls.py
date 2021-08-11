# アプリ用ルーティング定義ファイル
from django.urls import path
# 同じフォルダから、views.pyをインポート
from . import views

urlpatterns = [
    # トップのアクセスの時は、views.pyのindex関数を読み込む
    path('', views.index, name='list'),

    # update_taskにアクセスされた時、views.pyのupdateTaskの処理をします。
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),

    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
