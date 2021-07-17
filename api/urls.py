from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/', views.EndPoints),
    path('api/v1/todos/', views.Todos),
    path('api/v1/todos/<str:pk>/', views.SingleTodo),
]