from django import forms
from django.db.models import fields
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):

    # どのデータベースについていじっていくかを定義する
    class Meta:
        # モデルはimportしたTaskを使うよ！
        model=Task
        # 全てを編集するので、allにする
        fields='__all__'
        