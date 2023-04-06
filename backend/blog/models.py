from django.db import models
from datetime import datetime,date,time

class Message(models.Model):
	name = models.CharField(max_length=120,blank=False,null=False)
	L_name = models.CharField(max_length=120,blank=False,null=False)	
	email = models.EmailField(max_length=120,blank=False,null=False)
	message_body = models.TextField(max_length=2000,blank=False,null=False)
	create_at =  models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name + ' ' + self.L_name + ' - ' +  f"{self.create_at.strftime('%m/%d')}"