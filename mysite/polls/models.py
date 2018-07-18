from django.db import models

class Questoin(models.Model):
    question_tact = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.foreignKey(Question, on_delete=models.CASCADE)
    choice_text = model.CharField(max_length=200)
    votes = models.IntegerField(default=0)
