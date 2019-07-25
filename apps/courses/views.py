from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView
)
from django.urls import reverse_lazy
from .models import CourseModule, CoursePackage
from .forms import (
    CoursePackageAddForm,
    CourseModuleAddForm,
    CoursePackageEditForm,
)


class CoursePackageList(ListView):
    queryset = CoursePackage.objects.all()
    context_object_name = 'courses'
    template_name = 'course_list.html'


class CourseDetailView(DetailView):
    model = CoursePackage
    template_name = 'course_detail.html'
    context_object_name = 'course'

    def get_object(self):
        course_slug = self.kwargs.get("course_slug")
        return get_object_or_404(CoursePackage, course_slug=course_slug)


class CourseModuleDetailView(DetailView):
    template_name = 'module_view.html'
    context_object_name = 'module'

    def get_object(self):
        module_code = self.kwargs.get('module_code')
        return get_object_or_404(CourseModule, module_code=module_code)


class NewCourseView(CreateView):
    model = CoursePackage
    form_class = CoursePackageAddForm
    template_name = 'new_course.html'
    success_url = '/courses/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.course_author = self.request.user
        return super(NewCourseView, self).form_valid(form)


class CoursePackageDeleteView(DeleteView):
    success_url = reverse_lazy('course:list')
    template_name = 'coursepackage_confirm_delete.html'
    context_object_name = 'course'

    def get_object(self):
        slug = self.kwargs.get('course_slug')
        return get_object_or_404(CoursePackage, course_slug=slug)


class CourseEditView(UpdateView):
    form_class = CoursePackageEditForm
    template_name= 'course_edit.html'
    success_url= '/courses/'

    def get_object(self):
        course_slug = self.kwargs.get('course_slug')
        return get_object_or_404(CoursePackage, course_slug=course_slug)


class CourseModuleAddView(CreateView):
    form_class = CourseModuleAddForm
    template_name = 'module_add.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        course = get_object_or_404(CoursePackage, course_slug=self.kwargs.get('course_slug'))
        instance.course_package = course
        return super(CourseModuleAddView, self).form_valid(form)


class CourseModuleEditView(UpdateView):
    form_class = CourseModuleAddForm
    template_name = 'module_add.html'
    success_url = '/courses/'
    context_object_name = 'module'

    def get_object(self):
        code = self.kwargs.get('module_code')
        return get_object_or_404(CourseModule, module_code=code)

class CourseModuleDeleteView(DeleteView):
    form_class = CourseModuleAddForm
    template_name = 'coursemodule_confirm_delete.html'
    success_url = reverse_lazy('course:list')
    context_object_name = 'module'

    def get_object(self):
        code = self.kwargs.get('module_code')
        return get_object_or_404(CourseModule, module_code=code)
