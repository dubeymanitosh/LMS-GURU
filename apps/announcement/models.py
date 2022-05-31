from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User
from apps.subject.models import Subject

class Announcement(models.Model):
	subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
	issued_on = models.DateTimeField(auto_now_add= True)
	subject = models.CharField(max_length=100)
	description = QuillField(null=True,blank=True)
	file = models.FileField(upload_to="announcements",null=True,blank=True)
	announced_by = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.subject