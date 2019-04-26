from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>', views.category),
    path('categories', views.list_cates),
    path('<int:id>', views.showOne)
]