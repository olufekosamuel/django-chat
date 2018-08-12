from django.db import models
from django.contrib.auth.models import User


class channel(models.Model):
	name = models.CharField(max_length = 200)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
#Gets chat in channel
	def get_chat(self):
		return self.chat_set.all()


class chat(models.Model):
	channel = models.ForeignKey(channel, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content
