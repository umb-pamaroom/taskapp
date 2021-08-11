from django.shortcuts import render, redirect
# httpからのレスポンスを受け付けるようにする
from django.http import HttpResponse

# models.pyからデータベースのモデルをimport
from .models import *

# フォームからのデータを扱うために
from .forms import *

# インターフェースを担当する場所になる



def index(request):
    # models.pyのTaskクラスから、それぞれのデータを読み込む
    tasks=Task.objects.all()

    # forms.pyのTaskformをimport
    form=TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    # tasksというオブジェクトたちを、tasklistと定義するよ！
    # htmlでは、tasklistで使えるようにする
    context={'tasklist':tasks, 'form':form}
    # リクエストがあった場合に、taskappの中のindex.htmlを返す
    return render(request, 'taskapp/index.html', context)


# pkはプライマリーキー
def updateTask(request,pk):
    task=Task.objects.get(id=pk)

    form=TaskForm(instance=task)

    if request.method=="POST":
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, 'taskapp/update_task.html', context)



def deleteTask(request, pk):
    item=Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request, 'taskapp/delete.html', context)
