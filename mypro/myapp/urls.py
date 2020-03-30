from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_success/',views.user_success,name='user_success'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('Customer/',views.Customer,name='Customer'),
    path('signup_view/',views.signup_view,name='signup_view'),
]