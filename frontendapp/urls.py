from django.urls import path
from .import views


urlpatterns=[
	path('login/',views.loginpage, name="login"),
	path('register/',views.registerpage, name="register"),
	path('',views.homepage, name="home"),
	path('forms/',views.formpages, name="forms"),
	path('tables/',views.tablepages, name="tables"),
	path('departments/',views.departmentpages, name="departments"),
	path('sessions/<str:pk>/',views.sessionspages, name="sessions"),
	path('dept/<dept_id>/session/<str:pk>/students/',views.SessionStudentPageView, name="SessionStudents"),
	# view sessions compeleted by the student
	path('student/<stud_id>/completed-session/',views.StudentCompletedSessionPageView, name="completed-session"),
	# view all students result for a coomplete session in  a differnt view and age
	path('transcript/student/<student_id>/session/<session_id>/allsemesters/',views.StudentTranscriptPageView, name="completed-session"),
]  