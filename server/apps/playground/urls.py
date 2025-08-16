from django.urls import path
from server.apps.playground.views import hello_world, HelloWorldView

urlpatterns = [
    path("hello/", hello_world),
    path("hello-class/", HelloWorldView.as_view()),
]
