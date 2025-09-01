from django.urls import path
from server.apps.playground.views import hello_world, HelloWorldView
from server.apps.playground.views import (
    ItemViewSet,
)

urlpatterns = [
    path("hello/", hello_world),
    path("hello-class/", HelloWorldView.as_view()),
    path("items/", ItemViewSet.as_view()),
    path("items/id/<int:pk>/", ItemViewSet.as_view()),
    path("items/create/", ItemViewSet.as_view()),
    path("items/delete/<int:pk>/", ItemViewSet.as_view()),
]
