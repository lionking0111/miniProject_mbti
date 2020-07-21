from django.shortcuts import render
import requests

# Create your views here.
def intro(request):
    return render(request, 'mbti/intro.html')

def signin(request):
    return render(request, 'mbti/signin.html')

def question(request):
    return render(request, 'mbti/q1.html')

def result(request):
    return render(request, 'mbti/result.html')