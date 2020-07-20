#질문에 답을 한다.
#답을 고른다
#고른 답마다 값을 매긴다.
#값을 더한다.
#각 값이 더해진 비중만큼 한 성향을 결정한다.
#4가지의 성향을 합쳐 최종검사결과를 도출한다.
extraIntro = 50

question1 = ("")
question2 = ("2. 모처럼의 휴일, 그럴 때 나는?")
ques2Answer = {
"1" : "먹고, 자고, 먹고, 자고가 최고지", 
"2" : "밖은 위험해...집에서 최대한 활동해야지", 
"3" : "집은 너무 답답해, 혼자라도 나가야지!", 
"4" : "야! 뭐하냐?! 나와라! 놀자!놀자!"
}

print(ques2Answer)
myAnswer2 = int(input("답변 : "))

#print(myAnswer2)
if myAnswer2 == 1:
    extraIntro = extraIntro + 25

print(extraIntro)

question3 = ("")
question4 = ("")
question5 = ("")
question6 = ("")
question7 = ("")