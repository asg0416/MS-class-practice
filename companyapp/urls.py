from django.urls import path
from .views import index,second,create
urlpatterns = [
    path('second/', second, name="second"),
    path('create/', create, name="create"),
]