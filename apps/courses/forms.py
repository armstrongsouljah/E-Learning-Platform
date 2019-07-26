from django import forms
from .models import CoursePackage, CourseModule
from  .models import Rating


class RatingForm(forms.ModelForm):
    """ Form for enabling a student rate a course """
    class Meta:
        model = Rating
        fields = ('rating',)


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

    def clean_resourse(self):
        file = self.cleaned_data.get('resource')
        if file._size > 10485760:
            raise forms.ValidationError('File cannot be bigger than 10mb')
        return file
