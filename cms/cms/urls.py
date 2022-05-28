from django.contrib import admin
from django.urls import path
from cmsapp.views import home,dept,Adept,remove ,std,Astd,dele
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home , name="home"),
    path("dept/", dept , name="dept"),
    path("Adept/", Adept , name="Adept"),
    path("remove/<int:d>", remove , name="remove"),
    path("std/", std , name="std"),
    path("Astd/", Astd , name="Astd"),
    path("dele/<int:s>", dele , name="dele"),
]
