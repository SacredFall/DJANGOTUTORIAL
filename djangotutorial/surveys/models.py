from django.db import models
class Topic(models.Model):
    def __str__(self):
        return self.topic
    topic = models.CharField(max_length='200')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length='200')
    votes = models.IntegerField(default = 0)


# Create your models here.
