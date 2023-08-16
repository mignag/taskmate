from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.task + " - " + str(self.done)