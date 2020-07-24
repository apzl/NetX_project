from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as user_views



urlpatterns = [
    path('signup/', user_views.registerPage, name="signup"),
	path('profile/', user_views.profilePage, name="profile"),
	path('login/', auth_views.LoginView.as_view(template_name='login.html') , name="login"),
	path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout") 
]