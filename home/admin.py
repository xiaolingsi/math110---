from django.contrib import admin
from home import models
# Register your models here.
admin.site.register(models.TeacherInfo)
admin.site.register(models.StudentInfo)
admin.site.register(models.UserInfo)
admin.site.register(models.Course)
admin.site.register(models.Test_paper)
admin.site.register(models.Public_Test_paper)
admin.site.register(models.Pro_Test_paper)
admin.site.register(models.contest_Test_paper)
admin.site.register(models.Video)
admin.site.register(models.Notice)
admin.site.register(models.CourseData)
admin.site.register(models.Homework)
admin.site.register(models.Stu_Grade)
admin.site.register(models.Course_detial)
admin.site.register(models.Stu_Course)