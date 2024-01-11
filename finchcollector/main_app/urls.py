from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/new/', views.FinchCreate.as_view(), name='create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='delete'),
]