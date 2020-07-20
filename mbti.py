#질문에 답을 한다.
#답을 고른다
#고른 답마다 값을 매긴다.
#값을 더한다.
#각 값이 더해진 비중만큼 한 성향을 결정한다.     (50에서 + 한다)
#4가지의 성향을 합쳐 최종검사결과를 도출한다.
extraIntro = 50       #외향 내향 합친 변수= 50으로 잡음 

question1 = ("")
question2 = ("2. 모처럼의 휴일, 그럴 때 나는?")
ques2Answer = {
"1" : "먹고, 자고, 먹고, 자고가 최고지", 
"2" : "밖은 위험해...집에서 최대한 활동해야지", 
"3" : "집은 너무 답답해, 혼자라도 나가야지!", 
"4" : "야! 뭐하냐?! 나와라! 놀자!놀자!"
} #딕셔너리 

print(ques2Answer)
myAnswer2 = int(input("답변 : "))

#print(myAnswer2)
if myAnswer2 == 1:
    result2 = extraIntro + 12.5
    print(result2)

question3 = ("")
question4 = ("3. 어두운 숲을 지나는 당신, 무언가 내앞을 스쳐지나갔다. 그럴때 나는?")
ques4Answer = { 
    "1" : "뭐지? 신기하게 생겼었어!! 확인하고야 말겠다!",
    "2" : "토끼? 다람쥐? 비슷하게 생겼던거 같아. 대충 그렇게 생각하고 간다.",
    "3" : "위험할 수 있으니 조심하면서 가자",
    "4" : "이 숲에서 저런게 다닐리가 없어.. 다시 돌아가자"
}

print(ques4Answer)
myAnswer4 = input("답변 : ")
print(myAnswer4)
if myAnswer4 == 1:
    result4 = extraIntro - 25
    print(result4)

question5 = ("")
question6 = ("4. 꿈에 조상님이 나와 숫자 5개를 불러주셨다. 미쳐 하나를 듣지 못하고 깨버린나, 그럴때 나는?")
ques6Answer = {
    "1" : "드디어 내게도 이런 날이?!! 당장 복권을 사러가서 듣지 못한 숫자는 모두 해본다.",
    "2" : "오늘 좋은 일이 생기려나보다 즐거운 마음으로 생활해야지",
    "3" : "꿈은 꿈일뿐, 허상은 허상일뿐 평소와 같은 생활을 한다.",
    "4" : "무슨 꿈이었더라…?"
} 

print(ques6Answer)
myAnswer6 = input("답변 : ")
print(myAnswer6)
if myAnswer6 == 1:
    result6 = extraIntro + 25
    print(result6)
