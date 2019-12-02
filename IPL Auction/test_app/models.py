from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import now

# Create your models here.

class Login(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	team_cur_players= models.IntegerField(default=0)
	team_ruppe= models.FloatField(default=100)
	team_logo = models.ImageField(upload_to='static/images/')
	team_ihfew=models.CharField(null=True,max_length=30)

	def __str__(self):
		return self.user.username


class player(models.Model):
	player_name= models.CharField(max_length=30)
	player_team=models.CharField(null=True,max_length=30,default=False)
	player_basePrice=models.FloatField(null=True)
	player_soldprice = models.FloatField(null=True,default=None)
	player_logo = models.ImageField(upload_to='static/images/players',null=True)
	player_status=models.CharField(default=False,max_length=10)
	player_time= models.DateTimeField(default=now)

	def __str__(self):
		return self.player_name