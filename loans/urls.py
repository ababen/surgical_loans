from django.urls import path

from . import views
from .views import LoansList, LoanDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', LoansList.as_view(), name="loans_list"),
    path('<int:pk>', LoanDetail.as_view(), name="loans_detail")
]