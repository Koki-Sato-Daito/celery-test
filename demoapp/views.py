from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from demoapp.models import Widget
from demoapp.forms import WidgetForm
from config.tasks import count_widgets, rename_widget


class WidgetListView(View):
    def get(self, request, *args, **kwargs):
        # タスクの呼び出し
        result = count_widgets.delay()
        return HttpResponse(f'{result.id} : {result.status}')

class WidgetRenameView(View):
    def get(self, request, pk, *args, **kwargs):
        instance = Widget.objects.get(pk=pk)
        form = WidgetForm(instance=instance)
        return render(request, 'demoapp/rename.html', {'form': form})

    def post(self, request, pk, *args, **kwargs):
        name = request.POST['name']
        # タスクの呼び出し
        result = rename_widget.delay(pk, name)
        return HttpResponse(f'{result.id} : {result.status}')


