from django.urls import path

from demoapp.views import WidgetListView, WidgetRenameView, WidgetTaskView


appname="demoapp"
urlpatterns = [
    path('widget_count/', WidgetListView.as_view()),    
    path('widget_rename/<int:pk>/', WidgetRenameView.as_view()),
    path('tasks/<str:task_id>/', WidgetTaskView.as_view())
]
