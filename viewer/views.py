from django.shortcuts import render
from django.views import generic

from emocheck.models import Result


class IndexView(generic.ListView):
  template_name = 'viewer/index.html'
  model = Result
  paginate_by = 20


class DetailView(generic.DetailView):
  template_name = 'viewer/detail.html'
  model = Result
  context_object_name = 'result_detail'
