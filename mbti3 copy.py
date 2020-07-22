
extraIntro = 50       #외향/내향 초기 변수= 50 
sensIntu = 50         #감각/직관 초기 변수 = 50
thinkFeel = 50        #사고/감정 초기 변수 = 50
judgePerce = 50       #판단/인식 초기 변수 = 50

def firstClass(extraIntro): # E/I 관련문항
    
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

#E/I 2번문제    
     
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
#E/I 3번문제    
      
        question3 = ("3.새내기 배움터에서 가장 늦게 도착했다. 이 때, 나는 어디에 앉을 것인가?") #질문3
        ques3Answer = {
        "1" : "아무대나 앉아도 상관없다. 대신 혼자는 싫어", 
        "2" : "아는 사람이 있는지 찾아보고 앉는다.", 
        "3" : "빈공간이 있다면 어디든 상관없다.", 
        "4" : "들어온 입구에서 가장 가까운 쪽에 조심스레 앉는다."
        } #딕셔너리 
        print(question3)
        print(ques3Answer)

        myAnswer3 = int(input("답변 : "))

       
#E/I 4번문제 
      
        question4 = ("4.친구의 소개팅으로 만난 이상형, 그럴 때 나는?")  #질문4
        ques4Answer = {
        "1" : "그녀의 관심을 사기 위해 쉴틈없이 말을 한다.", 
        "2" : "어색한 분위기가 싫어 주도하여 먼저 말을 건넨다.", 
        "3" : "묻는 말에 대답하며, 되묻는 편이다. And you?", 
        "4" : "너무 부끄러워…말을 건넬 수가 없다.."
        } #딕셔너리 
        print(question4)
        print(ques4Answer)

        myAnswer4 = int(input("답변 : "))
firstClass(extraIntro)




def secondClass(sensIntu): # S/N 관련문항
    
# #S/N 1번문제
        question1 = ("5.어두운 숲을 지나는 당신, 무언가 내 앞을 스쳐지나갔다. 그럴 때 나는?") #질문1
        ques1Answer = {
        "1" : "뭐지? 신기하게 생겼었어!! 확인하고야 말겠다!",
        "2" : "토끼? 다람쥐? 비슷하게 생겼던거 같아. 대충 그렇게 생각하고 간다.",
        "3" : "위험할 수 있으니 조심하면서 가자",
        "4" : "이 숲에서 저런 게 다닐리가 없어… 다시 돌아가자"
        }
        print(question1)
        print(ques1Answer)
        myAnswer1 = int(input("답변 : "))

   

    #S/N 2번문제    
        
        question2 = ("6.꿈에 조상님이 나와 숫자 5개를 불러주셨다.. 미쳐 하나를 듣지 못하고 깨버린 나, 그럴 때 나는?") #질문2
        ques2Answer = {
        "1" : "드디어 내게도 이런 날이?!! 당장 복권을 사러가서 듣지 못한 숫자는 모두 해본다.", 
        "2" : "오늘 좋은 일이 생기려나보다 즐거운 마음으로 생활해야지", 
        "3" : "꿈은 꿈일뿐, 허상은 허상일뿐 평소와 같은 생활을 한다.", 
        "4" : "무슨 꿈이었더라…?"
        } #딕셔너리 
        print(question2)
        print(ques2Answer)

        myAnswer2 = int(input("답변 : "))

   

#     #S/N 3번문제    
     
        question3 = ("7.학점이 걸린 조별과제, 그 속에 나는 어떤 자세로 임할까??") #질문2
        ques3Answer = {
        "1" : "과정이 어떻든, 학점만 A+이면 되는거야!", 
        "2" : "내가 말을 제일 잘하니까, 내가 발표를 할게! ", 
        "3" : "이런 프로젝트 예전에 해본 적 있어! 내가 분업해줄게!", 
        "4" : "비록 학점은 D가 나와도, 우리는 최선을 다할거야"
        } #딕셔너리 
        print(question3)
        print(ques3Answer)

        myAnswer3 = int(input("답변 : "))



#     #S/N 4번문제    
        
        question4 = ("8.우리 동네에서 범죄가 발생했다. 그 때 나의 생각 및 행동은?") #질문2
        ques4Answer = {
        "1" : "당장 도어락과 방범창을 달아야겠어! 범죄로부터 벗어나려 행동한다.", 
        "2" : "세상이 참 흉흉하다..늦은 밤에는 돌아다니지 말아야지!", 
        "3" : "무슨일이지? 누가 어떻게 되었나? 하고 생각한 후 나가지 않는다.", 
        "4" : "범죄라구?!! 어떤 사건인지 눈으로 보고 싶어! 하고 현장으로 나가본다."
        } #딕셔너리 
        print(question4)
        print(ques4Answer)

        myAnswer4 = int(input("답변 : "))
secondClass(sensIntu)



def ThirdClass(thinkFeel): # T/F 관련문항
     
# #T/F 1번문제
        question1= ("9.직장 상사에게 엄청 혼난 친구, 그럴 때 나는?") #질문1
        ques1Answer = {
        "1" : "A to Z, 컨설팅을 시도한다. 이래서 너가 잘못했네! 이러면 더 좋을껄?",
        "2" : "왜 무슨일 있었는데? 당시 일을 묻고 본인 생각을 정리하며 말한다.",
        "3" : "오늘 힘들었겠다! 격려한다!",
        "4" : "이 XX 그 상사XX 내 앞으로 데려와 뚝배기 깨줄라니까!"
        }
        print(question1)
        print(ques1Answer)
        myAnswer1 = int(input("답변 : "))

       
    
#T/F 2번문제
        question2 = ("10.비 오는 날 여자친구와의 데이트중인 당신, 파전이 먹고싶다. 하지만, 여자친구는 아니라고 말하는데..그럴 때 당신은?") #질문1
        ques2Answer = {
        "1" : "자기야, 왜 비오는 날 파전이 생각나는지 알아? 바로 전을 부치는 소리와 빗소리가 같기 때문이야. 그러니 오늘 파전을 먹어야 해",
        "2" : "역시 비오는 날에는 파전이지!! 봐봐 오늘 전집에 줄을 섰다구!",
        "3" : "자기는 뭘 먹고 싶은데…? 아쉽지만 여자친구가 아니라고 하는데..",
        "4" : "오늘 파전이 별로구나?! 자기 먹고싶은 거 다 말해~ 자기 먹고싶은 걸로 먹자!"
        }
        print(question2)
        print(ques2Answer)
        myAnswer2 = int(input("답변 : "))


      
#T/F 3번문제
        question3 = ("11.친구를 위해 3시간 동안 머핀을 만들어서 줬는데, 내가 먹어봐도 심각하게 달다. 친구가 나에게 해줬으면 하는 말은?") 
        ques3Answer = {
        "1" : "날 위해서 3시간 만들었다고? 진짜 감동이야",
        "2" : "대박이다~! 너무 잘만들었다 멋있어!!",
        "3" : "여기에 견과류 넣으면 더 좋았을것 같아! ",
        "4" : "나쁘지 않은데? 근데 좀 단것 같아서 다음엔 덜 달게 하면 완벽할것 같아!"
        }
        print(question3)
        print(ques3Answer)
        myAnswer3 = int(input("답변 : "))

      
#T/F 4번문제
        question4 = ("12.친구가 시험을 망쳤다고 속상해 한다. 당신이 할 말은?") #질문1
        ques4Answer = {
        "1" : "이번에 어려웠어ㅠㅠ 다 못봤을거야 속상해 하지마..",
        "2" : "나도 망쳤어..,,인생..",
        "3" : "어디서 틀렸는데? 그 부분을 더 보완하면 다음엔 더 잘 볼수 있을거야!",
        "4" : "우울해 하지말고 다음 시험 준비하자~!"
        }
        print(question4)
        print(ques4Answer)
        myAnswer4 = int(input("답변 : "))
ThirdClass(thinkFeel)


def fourthClass(judgePerce): # J/P 관련문항

     
# #J/P 1번문제
        question1 = ("13.오랜시간 꺼진 핸드폰, 켜보니 수많은 카톡들이 쌓여있다. 이럴 때 나는?") #질문1
        ques1Answer = {
        "1" : "서둘러서 모두 읽고 답을 한다.",
        "2" : "원하는 것만 읽고 답을 한다.",
        "3" : "이미 많은 시간이 지났다. 그냥 읽기 처리 한다.",
        "4" : "급하면 연락이 또 오겠지..내 할 일을 한다."
        }
        print(question1)
        print(ques1Answer)
        myAnswer1 = int(input("답변 : "))

       


# #J/P 2번문제
        question2 = ("14.친구들과의 해외여행, 이럴 때 나의 역할은?") #질문1
        ques2Answer = {
        "1" : "친구들! 여행일정은 내게 맡기라구!",
        "2" : "일정은 내가 준비할테니, 나머지를 부탁해",
        "3" : "일단 비행기랑 숙소만 있으면 되지 뭐~ 그건 내가 할게",
        "4" : "와!!! 여행이야?!! 너무 좋다!! (그저 좋다..)"
        }
        print(question2)
        print(ques2Answer)
        myAnswer2 = int(input("답변 : "))

       


     
#J/P 3번문제
        question3 = ("15.오늘 하기로 한 공부를 다 못 끝낼 것 같다. 이럴때 나는?") 
        ques3Answer = {
        "1" : "미루면 스트레스 받으니까 어떻게든 오늘 끝내야 겠다!! ",
        "2" : "오늘 날샘 각이다..",
        "3" : "난 내일의 나를 믿어!",
        "4" : "집중 될때 해야 더 효율적이야~! 다음시간에~~"
        }
        print(question3)
        print(ques3Answer)
        myAnswer3 = int(input("답변 : "))

    
    


  
# #J/P 4번문제
        question4 = ("16.다이어리를 선물 받은나, 어떻게 활용할 것인가?") 
        ques4Answer = {
        "1" : "난 다이어리에 이렇게 정리하는거 못해..",
        "2" : "5장 이상 써본적이 없는데 ??",
        "3" : "12월까지 꾸준히 사용해야지~!!! 일정을 쓰기 시작 한다.",
        "4" : "다이어리 너덜너덜 해졌는데!! 새 다이어리 또한 그렇게 써야지!"
        }
        print(question4)
        print(ques4Answer)
        myAnswer4 = int(input("답변 : "))
fourthClass(judgePerce)





while(True):
    #print(myAnswer2)
    if myAnswer1 == 1:
        result1 = extraIntro + 17
        print(result1)
    elif myAnswer1 == 2:
        result1= extraIntro + 15
        print(result1)
    elif myAnswer1 == 3:
        result1= extraIntro + 11
        print(result1)
    elif myAnswer1 == 4:
        result1= extraIntro + 7
        print(result1)
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

    #print(myAnswer2)
    if myAnswer2 == 1:
        result2 = result1 + 8
        print(result2)
    elif myAnswer2 == 2:
        result2= result1 + 10 
        print(result2)
    elif myAnswer2 == 3:
        result2 = result1 + 13
        print(result2)
    elif myAnswer2 == 4:
        result2 = result1 + 19
        print(result2)
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

     #print(myAnswer3)
    if myAnswer3 == 1:
        result3 = result2 - 12
        print(result3)
       
    elif myAnswer3 == 2:
        result3= result2 - 14
        print(result3)
       
    elif myAnswer3 == 3:
        result3 = result2 - 6
        print(result3)
        
    elif myAnswer3 == 4:
        result3 = result2 - 18
        print(result3)
       
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        


        #print(myAnswer2)
    if myAnswer4 == 1:
        result4 = result3 -5
        print(result4)
     
    elif myAnswer4 == 2:
        result4 = result3 - 9
        print(result4)
        
    elif myAnswer4 == 3:
        result4 = result3 - 16
        print(result4)
       
    elif myAnswer4 == 4:
        result4 = result3 - 20
        print(result4)
        
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        


        #print(myAnswer2)
    if myAnswer1 == 1:
        result1 = sensIntu +  17
        print(result1)
        
    elif myAnswer1 == 2:
        result1= sensIntu +  15
        print(result1)
       
    elif myAnswer1 == 3:
        result1= sensIntu + 11   
        print(result1)
       
    elif myAnswer1 == 4:
        result1= sensIntu + 7
        print(result1)
       
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        


    #print(myAnswer2)
    if myAnswer2 == 1:
        result2 = result1 + 19
        print(result2)
       
    elif myAnswer2 == 2:
        result2= result1  + 13
        print(result2)
        
    elif myAnswer2 == 3:
        result2 = result1 + 10
        print(result2)
        
    elif myAnswer2 == 4:
        result2 = result1 + 8
        print(result2)
        
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        

        #print(myAnswer2)
    if myAnswer3 == 1:
        result3 = result2 -6
        print(result3)
        
    elif myAnswer3 == 2:
        result3= result2 -12
        print(result3)
       
    elif myAnswer3 == 3:
        result3 = result2 -14
        print(result3)
        
    elif myAnswer3 == 4:
        result3 = result2 -18
        print(result3)
       
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
       


    #print(myAnswer2)
    if myAnswer4 == 1:
        result4 = result3 -5
        print(result4)
        
    elif myAnswer4 == 2:
        result4= result3  -9
        print(result4)
        
    elif myAnswer4 == 3:
        result4 = result3 -16
        print(result4)
       
    elif myAnswer4 == 4:
        result4 = result3 -20
        print(result4)
       
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
     



    #print(myAnswer2)
    if myAnswer1 == 1:
        result1 = thinkFeel + 17
        print(result1)
        
    elif myAnswer1 == 2:
        result1= thinkFeel + 15
        print(result1)
       
    elif myAnswer1 == 3:
        result1= thinkFeel + 11
        print(result1)
        
    elif myAnswer1 == 4:
        result1= thinkFeel + 7
        print(result1)
       
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
       




    #print(myAnswer2)
    if myAnswer2 == 1:
        result2 = result1 + 19
        print(result2)
     
    elif myAnswer2 == 2:
        result2= result1 + 13
        print(result2)
        
    elif myAnswer2 == 3:
        result2= result1 + 10
        print(result2)
        
    elif myAnswer2 == 4:
        result2= result1 + 8
        print(result2)
        
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
       

#print(myAnswer2)
    if myAnswer3 == 1:
        result3 = result2 -6
        print(result3)
        
    elif myAnswer3 == 2:
        result3= result2 -12
        print(result3)
     
    elif myAnswer3 == 3:
        result3= result2 -14
        print(result3)
      
    elif myAnswer3 == 4:
        result3= result2 -18
        print(result3)
       
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
      


    #print(myAnswer2)
    if myAnswer4 == 1:
        result4 = result3 - 20
        print(result1)
       
    elif myAnswer4 == 2:
        result4= result3 - 16
        print(result1)
        
    elif myAnswer4 == 3:
        result4= result3 - 9
        print(result1)
        
    elif myAnswer4 == 4:
        result4 = result3 - 5
        print(result1)
       
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        

 #print(myAnswer2)
    if myAnswer1 == 1:
        result1 = judgePerce + 17
        print(result1)
         
    elif myAnswer1 == 2:
        result1= judgePerce + 15
        print(result1)
          
    elif myAnswer1 == 3:
        result1= judgePerce +11
        print(result1)
           
    elif myAnswer1 == 4:
        result1= judgePerce +7
        print(result1)
           
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        

 #print(myAnswer2)
    if myAnswer2 == 1:
        result2 = result1 + 19
        print(result2)
       
    elif myAnswer2 == 2:
        result2= result1 + 13
        print(result2)
       
    elif myAnswer2 == 3:
        result2= result1 + 10
        print(result2)
       
    elif myAnswer2 == 4:
        result2= result1 + 8
        print(result2)
        
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
       

    #print(myAnswer2)
    if myAnswer3 == 1:
        result3 = result2 - 6
        print(result3)
          
    elif myAnswer3 == 2:
        result3= result2 - 12
        print(result3)
         
    elif myAnswer3 == 3:
        result3= result2 - 14
        print(result3)
          
    elif myAnswer3 == 4:
        result3= result2 - 18
        print(result3)
         
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
            




        #print(myAnswer2)
    if myAnswer4 == 1:
        result4 = result3 -5
        print(result4)
           
    elif myAnswer4 == 2:
        result4= result3 -9
        print(result4)
            
    elif myAnswer4 == 3:
        result4= result3 - 16
        print(result4)
         
    elif myAnswer4 == 4:
        result4= result3 - 20
        print(result4)
         
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
         




def bye():
    if result4 > 50:
        return "E", result4
    else:
        return "I", result4
      
    if result4 > 50:
        return "S", result4
    else:
        return "N", result4
   
    if result4 > 50:
        return "T", result4
    else:
        return "F", result4

    if result4 > 50:
        return "J", result4
    else:
        return "P", result4

