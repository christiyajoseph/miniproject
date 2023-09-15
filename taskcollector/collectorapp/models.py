from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
# class Super(models.Model):
#     d_user=models.ForeignKey(User,on_delete=models.CASCADE)
#     class Meta:
#         abstract = True

class Course(models.Model):
    Course = models.CharField(max_length=150)

    def __str__(self):
        return self.Course
    

class Day(models.Model):
    days = models.CharField(max_length=150)

    def __str__(self):
        return self.days
           

class Task(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    day=models.ForeignKey(Day,on_delete=models.CASCADE)
    description = models.TextField() 
    Task=models.CharField(max_length=250) 
    def __str__(self):
        return self.Task
class Content(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    task=ChainedForeignKey(Task,
                               chained_field="Course",
                               chained_model_field="Course",
                               show_all=False,
                               auto_choose=False,
                               sort=True,
                               verbose_name= "Task")
         