from django.contrib import admin
from django.urls import include, path
from character import views as characterViews

urlpatterns = [
    path("", characterViews.index), # zmienić na party
    path("character/", include("character.urls")),
    path("user/", include("user.urls")),
    path("admin/", admin.site.urls),
]