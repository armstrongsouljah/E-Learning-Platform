from django import forms
from .models import CoursePackage, CourseModule

class CoursePackageAddForm(forms.ModelForm):
    class Meta:
        model = CoursePackage
        fields = ('course_name', 'course_details', )

class CoursePackageEditForm(forms.ModelForm):
    class Meta:
        model = CoursePackage
        fields = ('course_name', 'course_details', )


class CourseModuleAddForm(forms.ModelForm):
    """ Form for adding modules to a course package """

    class Meta:
        model = CourseModule
        fields = ['module_name', 'description', 'resource' ]
