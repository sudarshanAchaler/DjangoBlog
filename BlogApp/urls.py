from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login_page', views.LoginPage, name='login-page'),
    path('register_page', views.RegisterPage, name='register-page'),
    path('posts/', views.posts, name='posts'),
    path('about/', views.about, name='about'),
    path('writeForUs/', views.writeforus, name='writeforus'),
    path('post/<str:pk>/', views.Post1),
    path('addComment/', views.addComment),
    path('like/', views.like),
    path('loginUser/', views.loginUser),
    path('registerUser/', views.registerUser),
    path('logoutUser/', views.logoutUser, name='logout'),
    path('draftSubmission/', views.draftSubmission, name='draftSubmission'),
    path('searchResults/', views.searchPost, name='search'),
]