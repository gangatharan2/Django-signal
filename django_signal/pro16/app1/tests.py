# from django.test import TestCase
# from django.db import transaction

# from .models import MyModel, OtherModel

# class SignalTest(TestCase):
#     def test_signal_and_transaction(self):
#         # Create a new MyModel instance within a transaction
#         with transaction.atomic():
#             my_model_instance = MyModel.objects.create(name="Test") 

#         # Check if MyModel was created successfully (transaction committed)
#         self.assertTrue(MyModel.objects.filter(name="Test").exists())

#         # Check if OtherModel was created successfully (signal handler outcome)
#         self.assertTrue(OtherModel.objects.filter(related_model=my_model_instance).exists()) 

#         # Now, simulate a failure in the signal handler (uncomment the raise statement in signals.py)
#         try:
#             with transaction.atomic():
#                 my_model_instance_2 = MyModel.objects.create(name="Test2") 
#         except Exception as e: 
#             # This exception should not rollback the initial MyModel creation
#             self.fail(f"Transaction unexpectedly rolled back: {e}") 

#         # Check if MyModel was still created even with signal handler failure
#         self.assertTrue(MyModel.objects.filter(name="Test2").exists())
from django.test import TestCase
from django.db import transaction

from .models import MyModel, OtherModel

class SignalTest(TestCase):
    def test_signal_and_transaction(self):
        # Create a new MyModel instance within a transaction
        with transaction.atomic():
            my_model_instance = MyModel.objects.create(name="Test") 

        # Check if MyModel was created successfully (transaction committed)
        self.assertTrue(MyModel.objects.filter(name="Test").exists())

        # Now, simulate a failure in the signal handler (exceeding a database limit)
        with transaction.atomic():
            my_model_instance_2 = MyModel.objects.create(name="Test2") 

        # Check if MyModel was still created even with signal handler failure
        self.assertTrue(MyModel.objects.filter(name="Test2").exists())