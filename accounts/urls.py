from django.urls import path
from .import views

urlpatterns=[

	path('register/', views.SignUp.as_view()),
	path('login/', views.Login.as_view(), name="login"),
	path('logout/',views.logout_view)
]