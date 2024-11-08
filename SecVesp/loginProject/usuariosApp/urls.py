from django.urls import path

from usuariosApp.views import signUpView

urlpatterns = [
    path('signup/', signUpView.as_view(), name='signup')
]