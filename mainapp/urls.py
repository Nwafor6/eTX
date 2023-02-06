from django.urls import path
from rest_framework.routers import SimpleRouter
from .import views
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import DepartViewSet


router=SimpleRouter()
router.register('departments', DepartViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


# schema_view = get_swagger_view(title='Pastebin API')



urlpatterns = [
	path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path('departments/<str:pk>/add_admittedsession/', views.CreateAdmittedSession.as_view()),
	path('update_admittedsession/<str:pk>/', views.UpdateAdmittedSession.as_view()),
	path('delete_admittedsession/<str:pk>/', views.DestroyAdmittedSession.as_view()),
	# semester url#############
	path('add_semester/', views.CreateSemester.as_view()),
	path('update_semester/<str:pk>/', views.UpdateSemester.as_view()),
	path('delete_semester/<str:pk>/', views.DestroySemester.as_view()),
	#############################


	# student url#############
	path('add_student/', views.CreateStudent.as_view()),
	path('update_student/<str:pk>/', views.UpdateStudent.as_view()),
	path('delete_student/<str:pk>/', views.DestroyStudent.as_view()),
	#############################


	# sessioncompleted url#############
	path('add_sessioncompleted/', views.CreateSessionCompleted.as_view()),
	path('update_sessioncompleted/<str:pk>/', views.UpdateSessionCompleted.as_view()),
	path('delete_sessioncompleted/<str:pk>/', views.DestroySessionCompleted.as_view()),
	#############################

	# sessioncompleted url#############
	path('add_course/', views.CreateCourse.as_view()),
	path('update_course/<str:pk>/', views.UpdateCourse.as_view()),
	path('delete_course/<str:pk>/', views.DestroyCourse.as_view()),
	#############################

	# view all students admitted in a session#####
	path('department/<dept_id>/session/<str:pk>/students/', views.AdmittedSessionStudents.as_view()),
	#######################################################

	# # view all completed sessions od a students#####
	# path('student/<str:pk>/session/', views.StudentCompletedSession.as_view()),
	# #######################################################

	# view all completed sessions of a students#####
	path('student/<str:pk>/session/', views.StudentCompletedSession.as_view()),
	#######################################################

	# view all student's completed semester  in a session#####
	path('student/<str:pk>/session/<str:sess_id>/semester/', views.CompletedSemesters.as_view()),
	#######################################################

	#view all courses in the semester the student has completed#################
	path('student/<str:pk>/session/<str:sess_id>/semester/<str:sems_id>/', views.StudentSemesterCourse.as_view()),
	########################################
	#
	##############################
	# View the students CGPA for each semesters and sessions 
	path("student/cgpa/<str:pk>/", views.GetStudentCGPA.as_view()),


	path('upload/', views.examFieldUpload.as_view()),
	path('upload/student/', views.StudentUplaod.as_view()),
	path('search/', views.SearchStudent.as_view())






]+router.urls