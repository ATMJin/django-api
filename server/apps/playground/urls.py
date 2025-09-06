from django.urls import path, include
from server.apps.playground.views import hello_world, HelloWorldView
from server.apps.playground.views import (
    ItemViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)
router.register("items-v2", ItemViewSet)

urlpatterns = [
    path("hello/", hello_world),
    path("hello-class/", HelloWorldView.as_view()),
    # path("items/", ItemViewSet.as_view()),
    # path("items/id/<int:pk>/", ItemViewSet.as_view()),
    # path("items/create/", ItemViewSet.as_view()),
    # path("items/delete/<int:pk>/", ItemViewSet.as_view()),
    path("views/", include(router.urls)),  # Include the router URLs
]
