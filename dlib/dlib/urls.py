from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('books/', include('books.urls')),
    path('login/', views.signin),
    path('logout/', views.signout),
    path('signup/', views.signup)
]
