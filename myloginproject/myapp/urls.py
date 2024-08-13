from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view, home_view , logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', logout_view, name='logout'),
    
]
