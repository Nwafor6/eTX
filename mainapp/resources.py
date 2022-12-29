from import_export import resources
from .models import Student

class StudentResources(resources.ModelResource):
	class Meta:
		model=Student