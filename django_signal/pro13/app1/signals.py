from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

User=get_user_model()

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f"welcome mail sent to{instance.username}")
