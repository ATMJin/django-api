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
from django.urls import path
from server.apps.management.views import hello_world

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/practice/hello/", hello_world),
]
