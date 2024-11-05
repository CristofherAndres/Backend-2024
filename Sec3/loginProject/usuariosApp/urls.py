from django.urls import path

from usuariosApp.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]