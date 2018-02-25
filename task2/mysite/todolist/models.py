from django.db import models

# Create your models here.


class Affair(models.Model):
    affair_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.affair_text
