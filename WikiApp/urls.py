from django.urls import path
from .views import PageListView, create_page, index, CreateDataView, random_page

urlpatterns = [
    path('adder', PageListView.as_view(), name='page-list'),
    path('create/', create_page, name='create-page'),
    path('',index,name='index'),
    path('create_data/',CreateDataView.as_view(),name='create-data'),
    path('random_page/',random_page,name='random-page'),


]
