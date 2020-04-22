"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog_app/', include('blog_app.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views  # 72.
from django.urls import path, include  # 5.1
from users_app import views as users_views  # 44.
# why it works without double dot for users_app, when app module is located in parent directory
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # patterns are tested in top-down order, so put your home page higher
    path('register/', users_views.register, name='users_app-register'),  # 44.
    path('profile/', users_views.profile, name='users_app-profile'),  # 86.
    # path('login/', auth_views.LoginView.as_view(), name='login'),  # 73. commented at 74.
    path('login/', auth_views.LoginView.as_view(template_name='users_app/login.html'), name='login'),  # 75.
    path('logout/', auth_views.LogoutView.as_view(template_name='users_app/logout.html'), name='logout'),  # 79.
    path('password-reset',
         auth_views.PasswordResetView.as_view(template_name='users_app/password_reset.html'),
         name='password_reset'),
    path('', include('blog_app.urls')),  # 5.2; 8.; 10;
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
