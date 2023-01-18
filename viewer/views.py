from django.shortcuts import render
from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView

from emocheck.models import Result


class IndexView(generic.ListView):
  template_name = 'viewer/list.html'
  model = Result
  paginate_by = 20


class DetailView(generic.DetailView):
  template_name = 'viewer/detail.html'
  model = Result
  context_object_name = 'result_detail'


class ResultListJsonView(BaseDatatableView):
  model = Result
  columns = ['id', 'scan_time', 'hostname', 'emocheck_version', 'is_infected']
  order_columns = ['scan_time']
  
  def get_filter_method(self):
    return super().FILTER_ICONTAINS
