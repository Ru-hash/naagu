from django.urls import path
from .views import DressListView,DressDetailView,DressCreateView,DressUpdateView,DressDeleteView,search

app_name='dress'
urlpatterns = [
    path('', DressListView.as_view(),name='list'),
   
    path('create/', DressCreateView.as_view(),name='create'),
    path('detail/<int:pk>/', DressDetailView.as_view(),name='detail'), 
    path('delete/<int:pk>/', DressDeleteView.as_view(),name='delete'), 
    path('update/<int:pk>/', DressUpdateView,name='update'),
    path('search/<str:variety>/', search,name='search'),  
]
