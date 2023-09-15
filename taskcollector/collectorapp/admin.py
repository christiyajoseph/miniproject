from django.contrib import admin
from.models import Course,Day,Task,Content



   
class Display(admin.ModelAdmin):
    
    list_display=(
            'Course','day','description','Task') 
    actions= [Course]

    

# Register your models here.
admin.site.register(Course)
admin.site.register(Day)
admin.site.register(Task,Display)
admin.site.register(Content)
