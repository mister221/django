from django.urls import path

from . import views

urlpatterns = [
		
	path('',views.UserRegister,name='user-register'),
	path('login/',views.UserLogin,name='user-login'),
	path('logout/',views.UserLogout,name='user-logout'),	
	
]