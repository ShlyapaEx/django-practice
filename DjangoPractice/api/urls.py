from django.urls import path

from .views import main, test

urlpatterns = [
    path('', main),
    path('test/', test)
]
