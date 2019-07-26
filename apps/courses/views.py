from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
    FormView
)
from django.urls import reverse_lazy
from .models import CourseModule, CoursePackage, Rating
from .forms import (
    CoursePackageAddForm,
    CourseModuleAddForm,
    CoursePackageEditForm,
    RatingForm
)


class CoursePackageList(ListView):
    queryset = CoursePackage.objects.all()
    context_object_name = 'courses'
    template_name = 'course_list.html'


class CourseDetailView(DetailView, CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'course_detail.html'
    context_object_name = 'course'


    def get_object(self, *args, **kwargs):
        course_slug = self.kwargs.get("course_slug")
        return get_object_or_404(CoursePackage, course_slug=course_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        has_rated = Rating.objects.filter(student=self.request.user, course=self.get_object()).exists()
        context['average_rating'] = self.get_object().average_rating
        context['has_rated'] = has_rated
        context['form'] = RatingForm
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.student = self.request.user
        instance.course = self.get_object()
        return super().form_valid(form)

class RatingView(CreateView):
    model = Rating
    form_class = RatingForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.student = self.request.user.student
        instance.course = CoursePackage.objects.get(course_slug=self.kwargs.get('course_slug'))
        return super(RatingView, self).form_valid(form)


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
