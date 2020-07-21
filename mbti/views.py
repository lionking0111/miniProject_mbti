from django.shortcuts import render
from django.http import request, JsonResponse
import requests
from .models import MbtiResult

# Create your views here.
def intro(request):
    return render(request, 'mbti/intro.html')

def signin(request):
    return render(request, 'mbti/signin.html')

def Question(request):
    return render(request, 'mbti/q1.html')

def result(request):
    return render(request, 'mbti/result.html')

def inquiry(request):
    return render(request, 'mbti/info_inquiry.html')
# DB보기 함수
def showResult(request):
    mbtiResult = MbtiResult.objects.all()
    return render(request, '/show_result.html', {'list':mbtiResult})

def showQuestion(request):
    question = QuestionList.objects.all()
    return render(request, '/show_question.html',)




def index(request):
    return render(request, 'mbti/index_초기설정.html')

def mbti_exam1(request):
    return render(request, 'mbti/mbti_exam1.html')

question = [
    {
        'question1' : "1. 모임에서의 첫 시간, 다른 사람에게 소개할 때 내 모습은?",
        'ques1Answer' : {
            "1" : "자신감 넘치며 당당히 일어나서 말을 한다.",
            "2" : "아무렇지 않게 소개한다.",
            "3" : "저..저는..감사합니다...(쭈뼛쭈뼛)",
            "4" : "(아...이런 시간 지나가라..너무 싫다..)"
        }
    },
    {
        'question2' : "2. sldfjalsd"
        
    }

]

def mbti1(request):
    extraIntro = 50 

    myAnswer1 = request.GET.get('answer1')
    myAnswer1 = int(myAnswer1)
    if myAnswer1 == 1:
        result1 = extraIntro + 12.5
        print(result1)
    elif myAnswer1 == 2:
        result1= extraIntro + 6.25 
        print(result1)
    elif myAnswer1 == 3:
        result1= extraIntro - 6.25
        print(result1)
    elif myAnswer1 == 4:
        result1= extraIntro - 12.5
        print(result1)

    myAnswer2 = request.GET.get('answer2')
    myAnswer2 = int(myAnswer2)

    #print(myAnswer2)
    if myAnswer2 == 1:
        result2 = result1 - 12.5
        print(result2)
        
    elif myAnswer2 == 2:
        result2= result1 - 6.25 
        print(result2)
        
    elif myAnswer2 == 3:
        result2 = result1 + 6.25
        print(result2)
        
    elif myAnswer2 == 4:
        result2 = result1 + 12.5
        print(result2)
        
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        
#E/I 3번문제

    myAnswer3 = request.GET.get('answer3')
    myAnswer3 = int(myAnswer3)
    result3 = 0
    #print(myAnswer2)
    if myAnswer3 == 1:
        result3 = result2 + 12.5
        print(result3)
        
    elif myAnswer3 == 2:
        result3= result2 + 6.25 
        print(result3)
        
    elif myAnswer3 == 3:
        result3 = result2 - 6.25
        print(result3)
        
    elif myAnswer3 == 4:
        result3 = result2 - 12.5
        print(result3)


    result = {}
    if result3 > 50:
        result["a"] = 'E'
        result['score'] = result3
    else:
        result["a"] = 'I'
        result['score'] = result3


    return JsonResponse(result)
