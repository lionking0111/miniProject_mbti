from django.db import models

# Create your models here.
class inputClient(models.Model):
    nickname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    password = models.IntegerField(default=0)  
    email = models.EmailField(max_length=255, null=True)


class MbtiResult(models.Model):
    nickname = models.CharField(max_length=255)
    password = models.IntegerField(default=0)
    email = models.EmailField(max_length=255, null=True)
    
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


#db로 저장되는 함수를 구현해야함 