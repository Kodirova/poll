from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=256)
    option1 = models.CharField(max_length=256)
    option2 = models.CharField(max_length=256)
    option3 = models.CharField(max_length=256)
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)

    def total(self):
        return self.option1_count + self.option2_count + self.option3_count