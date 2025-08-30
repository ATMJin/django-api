from django.urls import path
from server.apps.playground.views import hello_world, HelloWorldView
from server.apps.playground.views import (
    GetAllItemsView,
    GetItemDetailView,
    GetNameItemsView,
    CreateItemView,
)

urlpatterns = [
    path("hello/", hello_world),
    path("hello-class/", HelloWorldView.as_view()),
    path("items/", GetAllItemsView.as_view()),
    path("items/id/<int:pk>/", GetItemDetailView.as_view()),
    path("items/name/<str:name>/", GetNameItemsView.as_view()),
    path("items/create/", CreateItemView.as_view()),
]
