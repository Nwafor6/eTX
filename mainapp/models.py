from django.db import models

# Create your models here.

class Department(models.Model):
	title=models.CharField(max_length=100,unique=True)

	def __str__(self):
		return self.title

class AdmittedSession(models.Model):
	session_title=models.CharField(max_length=100, unique=True, help_text="2018/2019")
	department=models.ManyToManyField(Department, blank=True)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.session_title

	@property
	def semester(self):
		return self.semester_set.all()


# for department in Department.objects.all():
# 				print(department.id)

class Semester(models.Model):
	title=models.CharField(max_length=100)
	session=models.ForeignKey(AdmittedSession, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.title} | {self.session}"

class Student(models.Model):
	admitted_session=models.ForeignKey(AdmittedSession, on_delete=models.SET_NULL, null=True, blank=False)
	department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
	name=models.CharField(max_length=200)
	reg_number=models.CharField(max_length=50, unique=True)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} | {self.reg_number}"


class SessionCompleted(models.Model):
	session_title=models.ForeignKey(AdmittedSession, on_delete=models.CASCADE, null=True, blank=True)
	semester=models.ManyToManyField(Semester)
	student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.student} | {self.session_title}"

class Course(models.Model):
	course_title=models.CharField(max_length=200)
	course_code=models.CharField(max_length=70)
	credit_load=models.PositiveIntegerField(default=0)
	semester=models.ForeignKey(Semester, on_delete=models.SET_NULL,null=True, blank=True)
	student=models.ForeignKey(Student, on_delete=models.CASCADE)
	test_score=models.PositiveIntegerField(default=0)
	exam_score=models.PositiveIntegerField(default=0)
	grade=models.CharField(max_length=20)
	session=models.ForeignKey(AdmittedSession, null=True, blank=False, on_delete=models.CASCADE)
	department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=False)
	# point=models.PositiveIntegerField(default=0)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.course_title

	@property
	def quality_point(self):
		A,B,C,D,E,F=5,4,3,2,1,0
		if self.grade =="A":
			
			return self.credit_load * 5 
		elif self.grade =="B":	
			return self.credit_load * 4
		elif self.grade =="C":
			return self.credit_load * 3
		elif self.grade =="D":
			return self.credit_load * 2
		elif self.grade =="E":
			return self.credit_load * 1
		elif self.grade =="F":
			return self.credit_load * 0
		return ""
	

