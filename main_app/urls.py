from django.urls import path
from . import views

urlpatterns = [
    path('', views.widgets, name='widgets'),
    path('delete/<int:pk>',views.delete_widget, name='delete_widget'),
]


