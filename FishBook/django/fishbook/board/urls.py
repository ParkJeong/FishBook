from django.urls import path
from .views import list, writeform, write, view, modify, modifyform, delete

app_name = "board"
urlpatterns = [
    path('list', list, name="list"),
    path('list/<int:page>', list, name="list"),
    path('writeform/<int:page>', writeform, name="writeform"),
    path('writeform/<int:no>/<int:page>', writeform, name="reply_writeform"),
    path('write/<int:page>', write, name="write"),
    path('<int:no>/<int:page>', view, name="view"),
    path('modify/<int:no>/<int:page>', modifyform, name="modifyform"),
    path('modify/<int:page>', modify, name="modify"),
    path('delete/<int:no>/<int:page>', delete, name="delete"),
]
