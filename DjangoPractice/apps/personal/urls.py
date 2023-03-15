from django.urls import include, path

# from .views import

urlpatterns = [
    path('session-auth/', include('rest_framework.urls'))
    # path('', main),
    # path('test/', test)
]
