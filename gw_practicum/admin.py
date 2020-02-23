from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Site
from .models import Preceptor
from .models import Department
from .models import DegreeLevel
from .models import Major
from .models import Student
from .models import PracticumDirector


# Register your models here.
class AllUserAdmin(UserAdmin):
    pass


admin.site.register(User, AllUserAdmin)
admin.site.register(Site)
admin.site.register(Preceptor)
admin.site.register(Department)
admin.site.register(DegreeLevel)
admin.site.register(Major)
admin.site.register(Student)
admin.site.register(PracticumDirector)