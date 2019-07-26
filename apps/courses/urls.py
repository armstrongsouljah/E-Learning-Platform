from django.urls import path
from apps.courses import views as c_views 
app_name = 'courses'
urlpatterns = [
   path('', c_views.CoursePackageList.as_view(), name='list'),
   path('new-course/', c_views.NewCourseView.as_view(), name='new-course'),
   path('<course_slug>/add-module/', c_views.CourseModuleAddView.as_view(), name='add-module'),
   path('<course_slug>/', c_views.CourseDetailView.as_view(), name='course-detail'),
   path('<course_slug>/edit-course/', c_views.CourseEditView.as_view(), name='course-edit'),
   path('<course_slug>/delete/', c_views.CoursePackageDeleteView.as_view(), name='course-delete'),
   path('<course_slug>/<module_code>/', c_views.CourseModuleDetailView.as_view(), name='module-detail'),
   path('<course_slug>/<module_code>/edit/', c_views.CourseModuleEditView.as_view(), name='module-edit'),
   path('<course_slug>/<module_code>/delete/', c_views.CourseModuleDeleteView.as_view(), name='module-delete'),
   path('<course_slug>/rate/', c_views.RatingView.as_view(), name='rate-course')

]