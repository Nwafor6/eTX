# from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets
from django.db import transaction
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from .resources import StudentResources
from tablib import Dataset
from .models import (AdmittedSession,Semester,Student,SessionCompleted,Course,Department)
from .serializers import (DepartmentSerializer,AdmittedSessionSerializer,SemesterSerializer,StudentSerializer,SessionCompletedSerializer,CourseSerializer,
	ExamFieldUploadSerializer,SudentFieldUploadSerializer,SearchSudentSerializer,ModifedAdmittedSessionSerializer)

# extra serializer imports
from .serializers import studentCompletedSerializer,StudentSemesterSerializer,ModifedCourseSerializer



class DepartViewSet(viewsets.ModelViewSet):
	queryset=Department.objects.all()
	serializer_class=DepartmentSerializer
	permission_classes=[IsAuthenticated]

# Admittedsession Api
class CreateAdmittedSession(generics.ListCreateAPIView):
	queryset=AdmittedSession.objects.all()
	serializer_class=AdmittedSessionSerializer
	permission_classes=[IsAuthenticated]


	def get(self, request, *args, **kwargs):
		department=Department.objects.get(pk=kwargs["pk"])
		admitted_session=department.admittedsession_set.all()
		serializer=self.serializer_class(admitted_session, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		session_title=request.POST["session_title"]
		if Department.objects.all().count() > 0:
			admitted_session=AdmittedSession.objects.create(session_title=session_title)
			Semester.objects.create(title="First Semester", session=admitted_session)
			Semester.objects.create(title="Second Semester", session=admitted_session)
			for department in Department.objects.all():
				admitted_session.department.add(department)
			serializer=self.serializer_class(admitted_session, many=False)
			return Response(serializer.data)
		else:
			return Response("You have to create departments first")

class UpdateAdmittedSession(generics.RetrieveUpdateAPIView):
	queryset=AdmittedSession.objects.all()
	serializer_class=AdmittedSessionSerializer
	permission_classes=[IsAuthenticated]

class DestroyAdmittedSession(generics.DestroyAPIView):
	queryset=AdmittedSession.objects.all()
	serializer_class=AdmittedSessionSerializer
	permission_classes=[IsAuthenticated]

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.delete()
		return Response('success')

#################################################
# semster Api
class CreateSemester(generics.ListCreateAPIView):
	queryset=Semester.objects.all()
	serializer_class=SemesterSerializer
	permission_classes=[IsAuthenticated]


	def get(self, request, *args, **kwargs):
		serializer=self.serializer_class(Semester.objects.all(), many=True)
		return Response(serializer.data)

class UpdateSemester(generics.RetrieveUpdateAPIView):
	queryset=Semester.objects.all()
	serializer_class=SemesterSerializer
	permission_classes=[IsAuthenticated]

class DestroySemester(generics.DestroyAPIView):
	queryset=Semester.objects.all()
	serializer_class=SemesterSerializer
	permission_classes=[IsAuthenticated]

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.delete()
		return Response('success')
############################################

#################################################
# student Api
class CreateStudent(generics.ListCreateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	permission_classes=[IsAuthenticated]


	def get(self, request, *args, **kwargs):
		serializer=self.serializer_class(Student.objects.all(), many=True)
		return Response(serializer.data)

class UpdateStudent(generics.RetrieveUpdateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	permission_classes=[IsAuthenticated]

class DestroyStudent(generics.DestroyAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	permission_classes=[IsAuthenticated]

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.delete()
		return Response('success')
############################################


#################################################
# sessioncompleted Api
class CreateSessionCompleted(generics.ListCreateAPIView):
	queryset=SessionCompleted.objects.all()
	serializer_class=SessionCompletedSerializer
	permission_classes=[IsAuthenticated]


	def get(self, request, *args, **kwargs):
		serializer=self.serializer_class(SessionCompleted.objects.all(), many=True)
		return Response(serializer.data)

class UpdateSessionCompleted(generics.RetrieveUpdateAPIView):
	queryset=SessionCompleted.objects.all()
	serializer_class=SessionCompletedSerializer
	permission_classes=[IsAuthenticated]

class DestroySessionCompleted(generics.DestroyAPIView):
	queryset=SessionCompleted.objects.all()
	serializer_class=SessionCompletedSerializer
	permission_classes=[IsAuthenticated]


	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.delete()
		return Response('success')
############################################


#################################################
# sessioncompleted Api
class CreateCourse(generics.ListCreateAPIView):
	queryset=Course.objects.all()
	serializer_class=CourseSerializer
	permission_classes=[IsAuthenticated]


	def get(self, request, *args, **kwargs):
		serializer=self.serializer_class(Course.objects.all(), many=True)
		return Response(serializer.data)

class UpdateCourse(generics.RetrieveUpdateAPIView):
	queryset=Course.objects.all()
	serializer_class=CourseSerializer
	permission_classes=[IsAuthenticated]

class DestroyCourse(generics.DestroyAPIView):
	queryset=Course.objects.all()
	serializer_class=CourseSerializer
	permission_classes=[IsAuthenticated]

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.delete()
		return Response('success')
############################################

# view all students admitted in the same year######
class AdmittedSessionStudents(generics.RetrieveUpdateAPIView):

	queryset=AdmittedSession.objects.all()
	serializer_class=AdmittedSessionSerializer
	permission_classes=[IsAuthenticated]

	def get(self, request, *args, **kwargs):
		department=Department.objects.get(id=self.kwargs["dept_id"])
		queryset=AdmittedSession.objects.get(id=self.kwargs['pk'], department=department)
		admittedstudents=queryset.student_set.filter(department=department)
		serializer=StudentSerializer(admittedstudents, many=True)

		return Response(serializer.data)

	def post(self, request,*args,**kwargs):
		reg_number=request.POST["reg_num"]
		print(reg_number)

		department=Department.objects.get(id=self.kwargs["dept_id"])
		queryset=AdmittedSession.objects.get(id=self.kwargs['pk'], department=department)
		admittedstudents=queryset.student_set.filter(department=department, reg_number=reg_number)
		serializer=StudentSerializer(admittedstudents, many=True)

		return Response(serializer.data)

########################################


# # view all sessions completed by the student ######
# class StudentCompletedSession(generics.RetrieveAPIView):
# 	queryset=Student.objects.all()
# 	serializer_class=StudentSerializer
# 	permission_classes=[IsAuthenticated]

# 	def get(self, request, *args, **kwargs):
# 		queryset=Student.objects.get(id=self.kwargs['pk'])
# 		studentcompletedsessions=queryset.sessioncompleted_set.all()
# 		print(studentcompletedsessions)
# 		serializer=studentCompletedSerializer(studentcompletedsessions, many=True)

# 		return Response(serializer.data)

# ########################################



# view all sessions completed by the student
class StudentCompletedSession(generics.RetrieveAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	permission_classes=[IsAuthenticated]

	def get(self, request, *args, **kwargs):
		queryset=Student.objects.get(id=self.kwargs['pk'])
		studentcompletedsessions=[session for session in AdmittedSession.objects.all() if session.id >= queryset.admitted_session_id]
		print(studentcompletedsessions)
		serializer=ModifedAdmittedSessionSerializer(studentcompletedsessions, many=True)


		return Response(serializer.data)

#####################################################################

# view all completed semester in the students completed session ######
class CompletedSemesters(generics.RetrieveAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	permission_classes=[IsAuthenticated]

	def get(self, request, *args, **kwargs):
		queryset=SessionCompleted.objects.get(id=self.kwargs['sess_id'], student=self.kwargs['pk'])
		semester=queryset.semester.all()
		serializer=StudentSemesterSerializer(semester, many=True)
		return Response(serializer.data)

########################################


# view all courses for the students has  completed ######
class StudentSemesterCourse(generics.RetrieveAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
	permission_classes=[IsAuthenticated]

	def get(self, request, *args, **kwargs):
		queryset=AdmittedSession.objects.get(id=self.kwargs['sess_id'])
		# AllSemester=queryset.semester_set.all()
		_courses=queryset.course_set.filter(Q(student=self.kwargs['pk'],session_id=self.kwargs['sess_id']))
		# print(_courses)
		# print(Student.objects.get(id=self.kwargs['pk']),"student")
		# semester_title=Semester.objects.get(id=self.kwargs['sems_id'])
		# print(semester_title.title,"jhhuhu")
		# semester=Semester.objects.get(title=semester_title.title,session_id=self.kwargs['sess_id'],)
		# print(semester)
		# courses=semester.course_set.filter(student=self.kwargs['pk'], semester=semester )
		serializer=ModifedCourseSerializer(_courses, many=True)
		return Response(serializer.data)

########################################



# #view to allow upload of student in excel document
class StudentUplaod(generics.CreateAPIView):
	serializer_class=SudentFieldUploadSerializer
	permission_classes=[IsAuthenticated]

	def post(self, request, *args, **kwargs):
		# student_resource=StudentResources
		dataset=Dataset()
		new_student=request.FILES['studentfile']
		count=0

		if not new_student.name.endswith('xlsx'):
			return Response("The document must be in .xlsx ")

		imported_data=dataset.load(new_student.read(), format='xlsx')
		with transaction.atomic():
			for data in imported_data:
				admitted_session=data[1]
				print(admitted_session,"admitted_session")
				name=data[2]
				print(name,"name")
				reg_number=data[3]
				print(reg_number,"reg_number")
				department=data[4]
				print(department,"department")
				try:
					Student.objects.get(reg_number=reg_number)
					return Response(f"FAILED !! Students with registration {reg_number} already exist ")
				except:
					pass
				try:
					admitted_session=AdmittedSession.objects.get(session_title=str(data[1]))
				except:
					admitted_session=data[1]
					transaction.set_rollback(True)# roll back if this error causes error
					return Response(f"{admitted_session} Session  does not exist")
				try:
					department=Department.objects.get(title=str(data[4]))
				except:
					department=data[4]
					transaction.set_rollback(True)# roll back if this error causes error
					return Response(f"{department} department  does not exist")

				Student.objects.create(
					admitted_session=admitted_session,
					name=name,
					reg_number=reg_number,
					department=department
					)
				count+=1
			return Response(f"Student(s) upload complete !!! Total= {count}")


###############################################################
# View for uploading exam excel files
class examFieldUpload(generics.CreateAPIView):
	serializer_class=ExamFieldUploadSerializer
	permission_classes=[IsAuthenticated]

	def post(self, request, *args, **kwargs):
		# course_resource=CourseResources()
		dataset= Dataset()
		file=request.FILES['examfile']
		count=0

		if not file.name.endswith('xlsx'):
			return Response("The document must be in .xlsx ")

		imported_data=dataset.load(file.read())
		with transaction.atomic():#Trap the loop in a transaction to have ability of rolling back
			for data in imported_data:
				course_title=data[1]
				course_code=data[2]
				credit_load=data[3]
				semester=data[4]
				print(semester)
				student=data[6]
				test_score=data[7]
				exam_score=data[8]
				grade=data[9]
				department=data[10]
				session=data[11]

				try:
					session=AdmittedSession.objects.get(session_title=str(data[11]))
				except:
					session=data[11]
					transaction.set_rollback(True)# roll back if this error causes error
					return Response(f"{session} Session  does not exist")

				try:
					department=Department.objects.get(title=str(data[10]))
				except:
					department=data[10]
					transaction.set_rollback(True)# roll back if this error causes error
					return Response(f" Department '{department}' does not exist, you may need to check spelling to create it!!")

				try:
					semester=Semester.objects.filter(title__icontains=semester, session=session)
				except:
					semester=data[4]
					transaction.set_rollback(True)# roll back if this error causes error
					return Response(f" semester with the title '{semester}' does not exist")

				try:
					student=Student.objects.get(reg_number=student)
				except:
					student=data[5]
					transaction.set_rollback(True)# roll back if this error causes error
					return Response(f"Student with the Registration number {student} does not exist")

				print(data[1], data[2], data[3],data[4],data[5],data[6], data[7],data[9], data[10])
				coure=Course.objects.create(

						course_title=course_title,
						course_code=course_code,
						credit_load=credit_load,
						semester=semester,
						student=student,
						test_score=test_score,
						exam_score=exam_score,
						grade=grade,
						session=session,
						department=department


					)
				count+=1
			return Response(f"upload complete !!! Total= {count}")

#search student by reggistration number and display all courses
class SearchStudent(generics.CreateAPIView):
	queryset=Course.objects.all()
	serializer_class=SearchSudentSerializer
	permission_classes=[IsAuthenticated]

	def post(self, request, *args, **kwargs):
		query=request.POST['reg_num']
		student=Student.objects.get(reg_number=query)
		courses=student.course_set.all()
		serializer=ModifedCourseSerializer(courses, many=True)

		return Response(serializer.data)