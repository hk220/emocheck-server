from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('data/', views.ResultListJsonView.as_view(), name='data'),
]
