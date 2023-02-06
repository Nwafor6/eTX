# from __future__ import unicode_literals
import decimal
from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework import generics, viewsets
from django.db import transaction
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from .resources import StudentResources
from tablib import Dataset
from .models import (AdmittedSession,Semester,Student,SessionCompleted,Course,Department, CGPA)
from .serializers import (DepartmentSerializer,AdmittedSessionSerializer,SemesterSerializer,StudentSerializer,SessionCompletedSerializer,CourseSerializer, 
	ExamFieldUploadSerializer,SudentFieldUploadSerializer,SearchSudentSerializer,ModifedAdmittedSessionSerializer)
# importing credit load checker function to prevent upload of result
from .import utils
# extra serializer imports
from .serializers import studentCompletedSerializer,StudentSemesterSerializer,ModifedCourseSerializer,StudentCGPASerializer



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
			order=0
			try:
				# Check if any session has previously been created to escape error
				if AdmittedSession.objects.all().exists():
					print("hello")
					order=AdmittedSession.objects.last().order+1

				# If no session, set the first order=0 
				else:
					order=0
				admitted_session=AdmittedSession.objects.create(session_title=session_title, order=order)
			except:
				return Response({"detail":'Session already exist'}, status=status.HTTP_400_BAD_REQUEST)
			Semester.objects.create(title="First Semester", session=admitted_session)
			Semester.objects.create(title="Second Semester", session=admitted_session)
			for department in Department.objects.all():
				admitted_session.department.add(department)
			serializer=self.serializer_class(admitted_session, many=False)
			return Response(serializer.data)
		else:
			return Response({'detail':"You have to create Departments first !!"},status=status.HTTP_400_BAD_REQUEST)

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
		print(queryset.order)
		# AllSemester=queryset.semester_set.all()
		_courses=queryset.course_set.filter(Q(student=self.kwargs['pk'],session_id=self.kwargs['sess_id']))
		student=Student.objects.get(id=self.kwargs['pk'])

		# Get all sesssion starting from the student's admitted session. 
		session=[session for session in AdmittedSession.objects.all() if session.id >= student.admitted_session_id]
		course=Course.objects.filter(student=student)
		# End get all session starting from the students admitted sessions

		first_total_point=0
		first_total_quality_point=0
		second_total_point=0
		second_total_quality_point=0
		for course in _courses:
			if course.semester.title == "First Semester":
				first_total_point +=course.credit_load
				first_total_quality_point +=course.quality_point
			else:
				second_total_point +=course.credit_load
				second_total_quality_point +=course.quality_point
		# sum first and second semester total-pt and total qpoint to get CGPA
		Max_total_point=first_total_point + second_total_point
		Max_total_quality_point=first_total_quality_point + second_total_quality_point
		# import division module to return a float
		cgpa=(Max_total_quality_point/Max_total_point)
		cgpa= '%.2f' % float(cgpa)#this cgpa is for just the current academic session 
		serializer=ModifedCourseSerializer(_courses, many=True)

		######################################### #This session brings the student's gpa for the previus sessions, add and computes the CGPA  
		# Filter GPA for the previous session that belongs to the student
		brought_fwd_gpa=CGPA.objects.filter(Q(student=self.kwargs['pk'], session__order__lt=queryset.order))
		brought_fwd_gpa_serializer=StudentCGPASerializer(brought_fwd_gpa, many=True)
		total_brought_fwd_gpa=0
		total_brought_cgpa=cgpa # set total_brought_cgpa=CGPA of the intinal session  so as to be used incase the output in the forloop returns zero(0)
		# Calculate the entire GPA for the previous session and find the average by dividing by the total count of sessions to produce the CGPS
		if brought_fwd_gpa:
			for _gpa in brought_fwd_gpa:
				print(_gpa.gpa,"gpa output")
				total_brought_fwd_gpa +=_gpa.gpa
			total_brought_cgpa='%.2f' % float(total_brought_fwd_gpa/brought_fwd_gpa.count()) # Here we divided the total GPA by the total number of academic sessions. This produces the students CGPA 
		return Response({"final_CGPA":total_brought_cgpa, "student_cgpa":brought_fwd_gpa_serializer.data,"Ftotalpt":first_total_point,"FtotalQpt":first_total_quality_point, "stotalpt":second_total_point, "stotalQpt": second_total_quality_point,"CGPA":cgpa, "serializer":serializer.data,"student_addmitted_seesion":student.admitted_session.session_title} )
		# return Response(serializer.data)

########################################

class GetStudentCGPA(generics.ListAPIView):
	serializer_class=StudentCGPASerializer
	queryset=CGPA.objects.all()
	permission_classes=[IsAuthenticated]

	def get(self, request, *args, **kwargs):
		queryset=CGPA.objects.filter(student=self.kwargs['pk'])
		serializer=self.serializer_class(queryset, many=True)
		return Response({"detail":serializer.data})


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
				# print(semester)
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
					semester=Semester.objects.get(title=semester, session=session)
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
				
				# print(data[1], data[2], data[3],data[4],data[5],data[6], data[7],data[9], data[10])

				#####################################
				# Checks to make sure the test is >=30 and exam <=100
				if test_score >30 or test_score < 0 :
					transaction.set_rollback(True)
					return Response(f"upload failed because {student}'s test score '{test_score}' is invalid")
				if exam_score >70 or exam_score < 0:
					transaction.set_rollback(True)
					return Response(f"upload failed because {student}'s exam score '{exam_score}' is invalid ")
				####################################################################

				# check if the student has exceeded the credit load limit before creating first
				if utils.creditLoadLimitChecker(session.id, semester.id, student.id) == True:
					if utils.checkCourseEixistence(course_code,session.id, student.id, semester.id) == True: 
						return Response(f"upload failed because {student} has this result already")
					course=Course.objects.create(

							course_title=course_title,
							course_code=course_code,
							credit_load=credit_load,
							semester=semester,
							student=student,
							test_score=test_score,
							exam_score=exam_score,
							grade=utils.gradeCalulator(test_score,exam_score),
							session=session,
							department=department
						)
					try:
						student_cgpa=CGPA.objects.get(session=session,student=student)
					except:
						student_cgpa=CGPA.objects.create(session=session,student=student)
					student_cgpa.gpa = utils.cgpaCalculator(student=student.id,session=session.id)
					student_cgpa.save()

				else:
					transaction.set_rollback(True)
					return Response(f"upload failed because {student} exceeded credit load")
				count+=1
			return Response(f"upload complete !!! Total= {count}")
		return Response(f"An error occoured")


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

