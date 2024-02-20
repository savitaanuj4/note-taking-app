from django.urls import path, include
from .views import signup_view, login_view, test_view
# from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('test/', test_view, name='test')
]
