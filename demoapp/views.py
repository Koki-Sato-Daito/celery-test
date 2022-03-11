from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult

from demoapp.models import Widget
from demoapp.forms import WidgetForm
from proj.tasks import count_widgets, rename_widget


class WidgetListView(View):
    """
    Widgetの総数を計算するタスクを呼び出す
    """
    def get(self, request, *args, **kwargs):
        # タスクの呼び出し
        result = count_widgets.delay()
        response = HttpResponse()
        response.write('<a href="/demoapp/tasks/{}/">タスクの結果</a>'.format(result.task_id))
        return response


class WidgetRenameView(View):
    """
    Widgetをリネームするタスクを呼び出す
    """
    def get(self, request, pk, *args, **kwargs):
        instance = Widget.objects.get(pk=pk)
        form = WidgetForm(instance=instance)
        return render(request, 'demoapp/rename.html', {'form': form})

    def post(self, request, pk, *args, **kwargs):
        name = request.POST['name']
        # タスクの呼び出し
        result = rename_widget.delay(pk, name)
        response = HttpResponse()
        response.write('<a href="/demoapp/tasks/{}">タスクの結果</a>'.format(result.task_id))
        return response


class WidgetTaskView(View):
    """
    タスクIDからタスクの状態を追跡する
    """
    def get(self, request, task_id, *args, **kwargs):
        task = AsyncResult(task_id)
        return HttpResponse(
                '<ul>' +
                f'<li>id = {task.id} </li>' +
                f'<li>status = {task.status} </li>' +
                f'<li>result = {task.result} </li>'+
                '</ul>'
        )
