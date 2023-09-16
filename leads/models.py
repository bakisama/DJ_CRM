from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass

class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.user.email
#Object relational mapping


class Lead(models.Model):

  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  age = models.IntegerField(default=0)
  agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
  #On Delete argument must be passed with Foreign Keys

  def __str__(self) -> str:
    return f"{self.first_name} {self.last_name}"

  # SOURCE_CHOICES = (
  #   ('YouTube', 'YouTube'),
  #   ('Google', 'Google'),
  #   ('Newsletter', 'Newsletter'),
  # )
  # phoned = models.BooleanField(default=False)
  # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
  # #these choices don't restrict what goes in the field
  
  # profile_picture = models.ImageField(blank=True, null=True)
  # #blank means we're submitting an empty string and null mean that there's no value in the DB
  # special_files = models.FileField(blank=True, null=True)
  

  
