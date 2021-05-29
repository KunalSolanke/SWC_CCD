from django.urls.conf import include
from home.router import router
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('api/',include(router.urls))
]