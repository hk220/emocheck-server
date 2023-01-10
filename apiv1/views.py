from emocheck.models import Result
from .serializers import ResultModelSerializer
from rest_framework import generics


class ResultListView(generics.ListCreateAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultModelSerializer


class ResultDetailView(generics.RetrieveAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultModelSerializer
