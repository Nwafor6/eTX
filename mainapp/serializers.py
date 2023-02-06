from rest_framework import serializers
from django.utils.timezone import now
from .models import (AdmittedSession,
Semester,
Student,
SessionCompleted,
Course,
Department,
CGPA,
)


class DepartmentSerializer(serializers.ModelSerializer):

	class Meta:
		model=Department
		fields='__all__'
		extra_kwargs={'id':{'read_only':True},}


class AdmittedSessionSerializer(serializers.ModelSerializer):
	department=DepartmentSerializer(many=True,required=False)
	class Meta:
		model=AdmittedSession
		fields='__all__'
		extra_kwargs={'id':{'read_only':True},'department':{'read_only':True},}

class SemesterSerializer(serializers.ModelSerializer):
	class Meta:
		model=Semester
		fields=['title','session']
		extra_kwargs={'id':{'read_only':True},}

class SemesterSerializer(serializers.ModelSerializer):
	session=AdmittedSessionSerializer(many=False)
	class Meta:
		model=Semester
		fields='__all__'
		extra_kwargs={'id':{'read_only':True},}

class StudentSerializer(serializers.ModelSerializer):
	admitted_session=AdmittedSessionSerializer(many=False)
	department=DepartmentSerializer(many=False)
	class Meta:
		model=Student
		fields=['id','department','admitted_session','name','reg_number','created']
		extra_kwargs={'id':{'read_only':True},}

class StudentCGPASerializer(serializers.ModelSerializer):
	# semester=SemesterSerializer(many=False)
	session=AdmittedSessionSerializer(many=False)
	student=StudentSerializer(many=False)
	class Meta:
		model=CGPA
		fields=["session","student", "gpa"]

# uncomment this to show the related fields in theri __unicode than id ###
class SessionCompletedSerializer(serializers.ModelSerializer):
	semester=SemesterSerializer(many=True)
	session_title=AdmittedSessionSerializer(many=False)
	student=StudentSerializer(many=False)
	class Meta:
		model=SessionCompleted
		fields=['id','session_title','semester','student','created']
		extra_kwargs={'id':{'read_only':True},'semesters':{'read_only':True}}


class CourseSerializer(serializers.ModelSerializer):
	session=AdmittedSessionSerializer(many=False)
	semester=SemesterSerializer(many=False)
	student=StudentSerializer(many=False)
	class Meta:
		model=Course
		fields=['department','course_title','course_code','credit_load','semester','student','test_score','exam_score','grade','session','created']
		extra_kwargs={'id':{'read_only':True},}


##########################################
#modified serializer classes
class ModifedAdmittedSessionSerializer(serializers.ModelSerializer):
	semester=SemesterSerializer(many=True)
	class Meta:
		model=AdmittedSession
		fields=['id','session_title','semester']
		extra_kwargs={'id':{'read_only':True},}

class studentCompletedSerializer(serializers.ModelSerializer):
	# semester=SemesterSerializer(many=True)
	session_title=AdmittedSessionSerializer(many=False)
	# student=StudentSerializer(many=False)
	class Meta:
		model=SessionCompleted
		fields=['id','session_title']
		extra_kwargs={'id':{'read_only':True}}


class StudentSemesterSerializer(serializers.ModelSerializer):
	session=ModifedAdmittedSessionSerializer(many=False)
	class Meta:
		model=Semester
		fields=['id','title','session']
		extra_kwargs={'id':{'read_only':True},}



class ModifedStudentSerializer(serializers.ModelSerializer):
	# admitted_session=AdmittedSessionSerializer(many=False)
	class Meta:
		model=Student
		fields=['name','reg_number','created']
		extra_kwargs={'id':{'read_only':True},}

class ModifedCourseSerializer(serializers.ModelSerializer):
	session=ModifedAdmittedSessionSerializer(many=False)
	semester=StudentSemesterSerializer(many=False)
	student=ModifedStudentSerializer(many=False)
	class Meta:
		model=Course
		fields=['course_title','course_code','credit_load',"quality_point",'semester','student','test_score','exam_score','grade','session']
		extra_kwargs={'id':{'read_only':True},}


class ExamFieldUploadSerializer(serializers.Serializer):
	examfile=serializers.FileField(max_length=None, allow_empty_file=False, use_url='media/examfiles')

class SudentFieldUploadSerializer(serializers.Serializer):
	studentfile=serializers.FileField(max_length=None, allow_empty_file=False, use_url='media/examfiles')	

class SearchSudentSerializer(serializers.Serializer):
	reg_num=serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)



