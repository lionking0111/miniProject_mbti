from django.db import models

# Create your models here.
class inputClient(models.Model):
    nickname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    password = models.IntegerField(default=0)    


class MbtiResult(models.Model):
    nickname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    extraScore = models.IntegerField(default=0)
    introScore = models.IntegerField(default=0)
    senseScore = models.IntegerField(default=0)
    intuiScore = models.IntegerField(default=0)
    thinkScore = models.IntegerField(default=0)
    feelScore = models.IntegerField(default=0)
    judgeScore = models.IntegerField(default=0)
    perceiScore = models.IntegerField(default=0)

class QuestionList(models.Model):
    question = models.CharField(max_length=255)

class AnswerList(models.Model):
    answer = models.CharField(max_length=255)

