from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Complain(models.Model):

	complain_user = models.ForeignKey(User, on_delete=models.CASCADE)
	complain_department=models.CharField(max_length=100)
	complain_subject = models.CharField(max_length = 100,help_text = "Enter the complain subject")
	department_head=models.CharField(max_length=100)
	recepient=models.CharField(max_length=100)
	complain_description=models.TextField(max_length=2000)
	date_posted = models.DateTimeField(default = timezone.now)
	NOT_VISITED = 'NV'
	VISITED = 'V'
	INPROCESS = 'IP'
	COMPLETED = 'C'
	status = (
        (NOT_VISITED, 'NV'),
        (VISITED, 'V'),
        (INPROCESS, 'IP'),
        (COMPLETED, 'C'),)
	status=models.CharField(max_length=2,choices=status,)

	def __str__(self):
		return self.complain_department



