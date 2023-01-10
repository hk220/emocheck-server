from django.urls import path
from . import views

urlpatterns = [
    path("result/", views.ResultListView.as_view()),
    path("result/<int:pk>/", views.ResultDetailView.as_view()),
]
