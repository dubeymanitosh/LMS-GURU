from django.db import models
from django.contrib.auth.models import User
from apps.classroom.models import Classroom

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(default='',max_length=100, null=True, blank=True)
	profile_pic = models.ImageField(default='avatar.jpg',upload_to="profile_pics/")
	phone_number = models.CharField(max_length=13,null=True,blank=True)
	whatsapp_number = models.CharField(max_length=13,null=True,blank=True)
	pending_invitations = models.ManyToManyField(Classroom)
	
	def __str__(self):
		return f'{self.user.username} Profile'