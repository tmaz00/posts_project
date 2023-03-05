from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# Function that will execute everytime the user is created
"""
If User is created the signal 'post_save' is generated and being received by
receiver
"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Function which saves created Profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()