from .models import AdmittedSession, Semester, Student, Course
# function to keep the student's number of credit load not to exceed 24
# The function takes three aguments which include the student_id, session_id, ssemester_id
# Then a filter is carried upon the course model to get all courses that fits these aquments
#Then  we sum all the credit loads if all the filtered course and return True if they are <= 24 else returns False

def creditLoadLimitChecker(session, semester, student):
	courses=Course.objects.filter(student=student, semester=semester,session=session)
	total_credit_load=0
	for course in courses:
		total_credit_load +=course.credit_load
	if total_credit_load < 24:
		print(total_credit_load)
		return True
	return False



# function to caluculate the cgpa
def cgpaCalculator(session,student):
	cgpa=0
	if Course.objects.all().exists():
		print(Course.objects.all().exists())
		courses=Course.objects.filter(student=student, session=session)
		total_credit_load=0
		total_quality_point=0
		cgpa=0
		print(courses,"courses")
		for course in courses:
			total_credit_load +=course.credit_load
			total_quality_point +=course.quality_point
		try:
			cgpa=total_quality_point/total_credit_load
		except:
			cgpa=0
		print(cgpa,"in utils")
		return cgpa

	return cgpa


# Function to confirm the grade of the student incase of error during computation by the lecturer
# the function will add the test and exam score andd using the standard grade will return the correct grade as an out put
def gradeCalulator(test_score, exam_score):
	if test_score + exam_score <=39 :
		return "F"
	elif test_score +exam_score <=44 : 
		return "E"
	elif test_score +exam_score <=49 : 
		return "D"

	elif test_score +exam_score <=59 : 
		return "C"
	elif test_score +exam_score <=69 : 
		return "B"

	elif test_score +exam_score <=100 : 
		return "A"

# Prevent multiple upload of a particular result more than once
#The function will take the student, acadmic session, course and check if it exist, if 
#if yes, cause a roll back and prevent upload else upload the resut

def checkCourseEixistence(course_code, session, student, semester):
	if Course.objects.filter(course_code=course_code, session=session, student=student, semester=semester):
		return True
	return False



	
