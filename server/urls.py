"""
server 專案的 URL 設定。

`urlpatterns` 列表將 URL 導向到對應的 view。更多資訊請參見:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
範例:
函式型 view
    1. 匯入:from my_app import views
    2. 新增 URL 到 urlpatterns:path('', views.home, name='home')
類別型 view
    1. 匯入:from other_app.views import Home
    2. 新增 URL 到 urlpatterns:path('', Home.as_view(), name='home')
包含其他 URLconf
    1. 匯入 include() 函式:from django.urls import include, path
    2. 新增 URL 到 urlpatterns:path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/practice/", include("server.apps.playground.urls")),
    path("api/docs/schema.json", SpectacularJSONAPIView.as_view(), name="schema"),
    path(
        "api/docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.authtoken")),
]
