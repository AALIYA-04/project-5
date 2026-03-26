from django.urls import path

from app3_app import views

urlpatterns = [
   path("",views.todo,name="todo")
]
