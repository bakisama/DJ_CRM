from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        "Agent", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        "Category",
        related_name="leads",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    category = models.ForeignKey
    # On Delete argument must be passed with Foreign Keys

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # Contacted, New, Converted, Unconverted

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)

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
