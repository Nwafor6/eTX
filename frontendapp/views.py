from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddSessionForm
from django.contrib.sites.shortcuts import get_current_site 

# Create your views here.


def loginpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	return render(request, 'accounts/login.html')

def registerpage(request):
	return render(request, 'accounts/register.html')



@login_required(login_url='login')
def homepage(request):
	return render(request, 'mainapp/index.html')

@login_required(login_url='login')
def formpages(request):
	return render(request, 'mainapp/basic_elements.html')

@login_required(login_url='login')
def tablepages(request):
	return render(request, 'mainapp/basic-table.html')

@login_required(login_url='login')
def departmentpages(request):
	current_site = get_current_site(request)
	form=AddSessionForm()
	return render(request, 'mainapp/departments.html',{'form':form,"domain":current_site})

@login_required(login_url='login')
def sessionspages(request,pk):
	current_site = get_current_site(request)
	form=AddSessionForm()
	return render(request, 'mainapp/admitted-sessions.html',{'form':form,"domain":current_site, "pk":pk})

@login_required(login_url='login')
def SessionStudentPageView(request,pk,dept_id):
	print(pk,"hsgdyh")
	form=AddSessionForm()
	return render(request, 'mainapp/students.html',{'pk':pk,"dept_id":dept_id})

@login_required(login_url='login')
def StudentCompletedSessionPageView(request,stud_id):
	
	return render(request, 'mainapp/StudentsCompletedSession.html',{"stud_id":stud_id})

def handler404(request, exception):
	return render(request, 'mainapp/404.html', status=404)