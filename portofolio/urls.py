from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

def home(request):
    return render(request, "base.html")  # ini akan render templates/base.html

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),  # buka localhost:8000 langsung render base.html
    path("", include("main.urls")),
]
