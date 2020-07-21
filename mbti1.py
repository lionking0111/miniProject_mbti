#질문에 답을 한다.
#답을 고른다
#고른 답마다 값을 매긴다.
#값을 더한다.
#각 값이 더해진 비중만큼 한 성향을 결정한다.     (50에서 + 한다)
#4가지의 성향을 합쳐 최종검사결과를 도출한다.

extraIntro = 50       #외향/내향 초기 변수= 50 
sensIntu = 50         #감각/직관 초기 변수 = 50
thinkFeel = 50        #사고/감정 초기 변수 = 50
judgePerce = 50       #판단/인식 초기 변수 = 50

def firstClass(extraIntro): # E/I 관련문항
    while True:
#E/I 1번문제
        question1 = ("1. 모임에서의 첫 시간, 다른 사람에게 소개할 때 내 모습은?") #질문1
        ques1Answer = {
        "1" : "자신감 넘치며 당당히 일어나서 말을 한다.",
        "2" : "아무렇지 않게 소개한다.",
        "3" : "저..저는..감사합니다...(쭈뼛쭈뼛)",
        "4" : "(아...이런 시간 지나가라..너무 싫다..)"
        }
        print(question1)
        print(ques1Answer)
        myAnswer1 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer1 == 1:
            result1 = extraIntro + 12.5
            print(result1)
            break
        elif myAnswer1 == 2:
            result1= extraIntro + 6.25 
            print(result1)
            break
        elif myAnswer1 == 3:
            result1= extraIntro - 6.25
            print(result1)
            break
        elif myAnswer1 == 4:
            result1= extraIntro - 12.5
            print(result1)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break
#E/I 2번문제    
    while True:    
        question2 = ("2. 모처럼의 휴일, 그럴 때 나는?") #질문2
        ques2Answer = {
        "1" : "먹고, 자고, 먹고, 자고가 최고지", 
        "2" : "밖은 위험해...집에서 최대한 활동해야지", 
        "3" : "집은 너무 답답해, 혼자라도 나가야지!", 
        "4" : "야! 뭐하냐?! 나와라! 놀자!놀자!"
        } #딕셔너리 
        print(question2)
        print(ques2Answer)

        myAnswer2 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer2 == 1:
            result2 = result1 - 12.5
            print(result2)
            break
        elif myAnswer2 == 2:
            result2= result1 - 6.25 
            print(result2)
            break
        elif myAnswer2 == 3:
            result2 = result1 + 6.25
            print(result2)
            break
        elif myAnswer2 == 4:
            result2 = result1 + 12.5
            print(result2)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break
#E/I 3번문제
    while True:    
        question3 = ("3. 3번문제") #질문2
        ques3Answer = {
        "1" : "1번보기", 
        "2" : "2번보기", 
        "3" : "3번보기", 
        "4" : "4번보기"
        } #딕셔너리 
        print(question3)
        print(ques3Answer)

        myAnswer3 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer3 == 1:
            result3 = result2 + 12.5
            print(result3)
            break
        elif myAnswer3 == 2:
            result3= result2 + 6.25 
            print(result3)
            break
        elif myAnswer3 == 3:
            result3 = result2 - 6.25
            print(result3)
            break
        elif myAnswer3 == 4:
            result3 = result2 - 12.5
            print(result3)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break
#E/I 4번문제
    while True:    
        question4 = ("4. 4번문제") #질문2
        ques4Answer = {
        "1" : "1번보기", 
        "2" : "2번보기", 
        "3" : "3번보기", 
        "4" : "4번보기"
        } #딕셔너리 
        print(question4)
        print(ques4Answer)

        myAnswer4 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer4 == 1:
            result4 = result3 + 12.5
            print(result4)
            break
        elif myAnswer4 == 2:
            result4= result3 + 6.25 
            print(result4)
            break
        elif myAnswer4 == 3:
            result4 = result3 - 6.25
            print(result4)
            break
        elif myAnswer4 == 4:
            result4 = result3 - 12.5
            print(result4)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break
#E/I 5번문제
    while True:    
        question5 = ("5. 5번문제") #질문2
        ques5Answer = {
        "1" : "1번보기", 
        "2" : "2번보기", 
        "3" : "3번보기", 
        "4" : "4번보기"
        } #딕셔너리 
        print(question5)
        print(ques5Answer)

        myAnswer5 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer5 == 1:
            result5 = result4 + 12.5
            print(result5)
            break
        elif myAnswer5 == 2:
            result5= result4 + 6.25 
            print(result5)
            break
        elif myAnswer5 == 3:
            result5 = result4 - 6.25
            print(result5)
            break
        elif myAnswer5 == 4:
            result5 = result4 - 12.5
            print(result5)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break

    if result5 > 50:
        return "E", result5
    else:
        return "I", result5

firstType, typeScore = firstClass(extraIntro)
print(firstType)
print(typeScore)

#----------------------------------------------------------------

def secondClass(sensIntu): # S/N 관련문항
    while True:
#S/N 1번문제
        question1 = ("1. 모임에서의 첫 시간, 다른 사람에게 소개할 때 내 모습은?") #질문1
        ques1Answer = {
        "1" : "자신감 넘치며 당당히 일어나서 말을 한다.",
        "2" : "아무렇지 않게 소개한다.",
        "3" : "저..저는..감사합니다...(쭈뼛쭈뼛)",
        "4" : "(아...이런 시간 지나가라..너무 싫다..)"
        }
        print(question1)
        print(ques1Answer)
        myAnswer1 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer1 == 1:
            result1 = extraIntro + 12.5
            print(result1)
            break
        elif myAnswer1 == 2:
            result1= extraIntro + 6.25 
            print(result1)
            break
        elif myAnswer1 == 3:
            result1= extraIntro - 6.25
            print(result1)
            break
        elif myAnswer1 == 4:
            result1= extraIntro - 12.5
            print(result1)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break
#S/N 2번문제    
    while True:    
        question2 = ("2. 모처럼의 휴일, 그럴 때 나는?") #질문2
        ques2Answer = {
        "1" : "먹고, 자고, 먹고, 자고가 최고지", 
        "2" : "밖은 위험해...집에서 최대한 활동해야지", 
        "3" : "집은 너무 답답해, 혼자라도 나가야지!", 
        "4" : "야! 뭐하냐?! 나와라! 놀자!놀자!"
        } #딕셔너리 
        print(question2)
        print(ques2Answer)

        myAnswer2 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer2 == 1:
            result2 = result1 - 12.5
            print(result2)
            break
        elif myAnswer2 == 2:
            result2= result1 - 6.25 
            print(result2)
            break
        elif myAnswer2 == 3:
            result2 = result1 + 6.25
            print(result2)
            break
        elif myAnswer2 == 4:
            result2 = result1 + 12.5
            print(result2)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break
#S/N 3번문제
    while True:    
        question3 = ("3. 3번문제") #질문2
        ques3Answer = {
        "1" : "1번보기", 
        "2" : "2번보기", 
        "3" : "3번보기", 
        "4" : "4번보기"
        } #딕셔너리 
        print(question3)
        print(ques3Answer)

        myAnswer3 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer3 == 1:
            result3 = result2 + 12.5
            print(result3)
            break
        elif myAnswer3 == 2:
            result3= result2 + 6.25 
            print(result3)
            break
        elif myAnswer3 == 3:
            result3 = result2 - 6.25
            print(result3)
            break
        elif myAnswer3 == 4:
            result3 = result2 - 12.5
            print(result3)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break
#S/N 4번문제
    while True:    
        question4 = ("4. 4번문제") #질문2
        ques4Answer = {
        "1" : "1번보기", 
        "2" : "2번보기", 
        "3" : "3번보기", 
        "4" : "4번보기"
        } #딕셔너리 
        print(question4)
        print(ques4Answer)

        myAnswer4 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer4 == 1:
            result4 = result3 + 12.5
            print(result4)
            break
        elif myAnswer4 == 2:
            result4= result3 + 6.25 
            print(result4)
            break
        elif myAnswer4 == 3:
            result4 = result3 - 6.25
            print(result4)
            break
        elif myAnswer4 == 4:
            result4 = result3 - 12.5
            print(result4)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break
#S/N 5번문제
    while True:    
        question5 = ("5. 5번문제") #질문2
        ques5Answer = {
        "1" : "1번보기", 
        "2" : "2번보기", 
        "3" : "3번보기", 
        "4" : "4번보기"
        } #딕셔너리 
        print(question5)
        print(ques5Answer)

        myAnswer5 = int(input("답변 : "))

        #print(myAnswer2)
        if myAnswer5 == 1:
            result5 = result4 + 12.5
            print(result5)
            break
        elif myAnswer5 == 2:
            result5= result4 + 6.25 
            print(result5)
            break
        elif myAnswer5 == 3:
            result5 = result4 - 6.25
            print(result5)
            break
        elif myAnswer5 == 4:
            result5 = result4 - 12.5
            print(result5)
            break
        else:
            print("잘못된 명령입니다. 다시 입력하세요.")
            break

    if result5 > 50:
        return "S", result5
    else:
        return "N", result5

secondType, typeScore2 = secondClass(sensIntu)
print(secondType)
print(typeScore2) 

myMbti = firstType + secondType
myExtraIntro ={typeScore, 100 - typeScore} #반대성향값
mySensIntu = {typeScore2, 100 - typeScore2} #반대성향값

print(myMbti)
print(myExtraIntro)
print(mySensIntu)
# myMbtiScore = {myExtraIntro, mySensIntu}
# totalMbti=[myMbtiScore]

# totalMbti +=1
# dbMbti.append[totalMbti]
