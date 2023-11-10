from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserVerifyView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registr/', RegisterView.as_view(), name='register'),
    path('confirm/<int:pk>/', UserVerifyView.as_view(), name='confirming'),

]
