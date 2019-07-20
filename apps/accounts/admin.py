from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserAdminRegisterForm, UserAdminUpdateForm

# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = UserAdminUpdateForm
    add_form = UserAdminRegisterForm

    list_display = ('email', 'admin')
    list_filter = ('admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('student', 'instructor')}),
        ('Permissions', {'fields': ('admin', 'staff')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'student', 'instructor', 'admin', 'staff', 'password', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
