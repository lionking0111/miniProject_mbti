from django.db import models

# Create your models here.
class inputClient(models.Model):
    nickname = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=10, null=True)
    password = models.IntegerField(default=0, null=True)  
    email = models.EmailField(max_length=255, null=True)
    
class MbtiResult(models.Model):
    nickname = models.CharField(max_length=255, null=True)
    password = models.IntegerField(default=0, null=True)
    email = models.EmailField(max_length=255, null=True)
    extraScore = models.IntegerField(default=0)
    introScore = models.IntegerField(default=0)
    senseScore = models.IntegerField(default=0)
    intuiScore = models.IntegerField(default=0)
    thinkScore = models.IntegerField(default=0)
    feelScore = models.IntegerField(default=0)
    judgeScore = models.IntegerField(default=0)
    perceiScore = models.IntegerField(default=0)
    owner = models.ForeignKey(inputClient, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s %d %d %d %d %d %d %d %d' % (self.email, self.extraScore, self.introScore , 
        self.senseScore, self.intuiScore, self.thinkScore, self.feelScore, self.judgeScore, self.perceiScore)

class QuestionList(models.Model):
    question = models.CharField(max_length=255)

class AnswerList(models.Model):
    answer = models.CharField(max_length=255)

#db로 저장되는 함수를 구현해야함 