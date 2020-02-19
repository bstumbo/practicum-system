from django.contrib import admin
from .models import User
from .models import Site
from .models import Preceptor
from .models import Department
from .models import DegreeLevel
from .models import Major

# Register your models here.
admin.site.register(User)
admin.site.register(Site)
admin.site.register(Preceptor)
admin.site.register(Department)
admin.site.register(DegreeLevel)
admin.site.register(Major)