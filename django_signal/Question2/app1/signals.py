from django.dispatch import receiver
from .models import MyModel

def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}") 
    # perform signal logic here 

# Connect the signal handler to the post_save signal for MyModel
from django.db.models.signals import post_save
post_save.connect(my_signal_handler, sender=MyModel)