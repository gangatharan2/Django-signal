# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import MyModel, OtherModel 

# @receiver(post_save, sender=MyModel)
# def my_signal_handler(sender, instance, created, **kwargs):
#     try:
#         # Simulate a potential failure (e.g., a database constraint violation)
#         # Uncomment the following line to simulate a failure:
#         # raise Exception("Signal handler failed intentionally.") 
#         OtherModel.objects.create(related_model=instance) 
#     except Exception as e:
#         # Log the error instead of just printing
#         import logging
#         logger = logging.getLogger(__name__)
#         logger.error(f"Signal handler failed: {e}")
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MyModel, OtherModel 

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    try:
        # Simulate a potential failure (e.g., exceeding a database limit)
        for _ in range(1000):  # This might exceed a database constraint
            OtherModel.objects.create(related_model=instance) 
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Signal handler failed: {e}")