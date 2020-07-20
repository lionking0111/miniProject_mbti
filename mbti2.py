#질문에 답을 한다.
#답을 고른다
#고른 답마다 값을 매긴다.
#값을 더한다.
#각 값이 더해진 비중만큼 한 성향을 결정한다.   (50에서 + 한다)
#4가지의 성향을 합쳐 최종검사결과를 도출한다.
     #외향 내향 합친 변수= 50으로 잡음 
#print(myAnswer2)



extraIntro = 50 
a =50 
def thirdclass(extraIntro):  #전역함수 값을 받으려면 함수 매개변수 써야함
    
    while True:
        
        question5 = ("5.직장 상사에게 엄청 혼난 친구, 그럴 때 나는?")
        ques5Answer = {
        "1" : "A to Z, 컨설팅을 시도한다. 이래서 너가 잘못했네! 이러면 더 좋을껄?", 
        "2" : "왜 무슨일 있었는데? 당시 일을 묻고 본인 생각을 정리하며 말한다.", 
        "3" : "오늘 힘들었겠다! 격려한다!", 
        "4" : "이 XX 그 상사XX 내 앞으로 데려와 뚝배기 깨줄라니까!"
        } #딕셔너리 

        print(ques5Answer)
        myAnswer5 = int(input("답변 : "))

        if myAnswer5 == 1:
            result6 = extraIntro + 12.5
            print(result6)
            break

        elif myAnswer5 == 2:
            result6 = extraIntro + 6.25
            print(result6)
            break

        elif myAnswer5 == 3:
            result6 = extraIntro - 6.25
            print(result6)
            break

        elif myAnswer5 == 4:
            result6 = extraIntro - 12.5
            print(result6)
            break

        else:
            print("잘못입력했습니다.")
            break
   
        
    while True:    
        
        question6 = ("6.비 오는 날 여자친구와의 데이트중인 당신, 파전이 먹고싶다. 하지만, 여자친구는 아니라고 말하는데..그럴 때 당신은?")
        ques6Answer = {
        "1" : "자기야, 왜 비오는 날 파전이 생각나는지 알아? 바로 전을 부치는 소리와 빗소리가 같기 때문이야. 그러니 오늘 파전을 먹어야 해", 
        "2" : "역시 비오는 날에는 파전이지!! 봐봐 오늘 전집에 줄을 섰다구!", 
        "3" : "자기는 뭘 먹고 싶은데…? 아쉽지만 여자친구가 아니라고 하는데..", 
        "4" : "오늘 파전이 별로구나?! 자기 먹고싶은 거 다 말해~ 자기 먹고싶은 걸로 먹자!"
        }  

        print(ques6Answer)
        myAnswer6 = int(input("답변 : "))

        if myAnswer6 == 1:
            result7 = result6 + 12.5
            print(result7)
            break

        elif myAnswer6 == 2:
            result7 = result6 + 6.25
            print(result7)
            break

        elif myAnswer6 == 3:
            result7 = result6 - 6.25
            print(result7)
            break

        elif myAnswer6 == 4:
            result7 = result6 - 12.5
            print(result7)
            break

        else:
            print("잘못입력했습니다.")
            break
    if result6 > 50:
        return "T" , result6
    else :
        return "F" , result6

e,f= thirdhclass(a)

print(e)
print(f)

    
def fourthclass(a): 
    while True:    
        
        question7 = ("7.오랜시간 꺼진 핸드폰, 켜보니 수많은 카톡들이 쌓여있다. 이럴 때 나는?")
        ques7Answer = {
        "1" : "서둘러서 모두 읽고 답을 한다.", 
        "2" : "원하는 것만 읽고 답을 한다.", 
        "3" : "이미 많은 시간이 지났다. 그냥 읽기 처리 한다.", 
        "4" : "급하면 연락이 또 오겠지..내 할 일을 한다."
        }  

        print(ques7Answer)
        myAnswer7 = int(input("답변 : "))

        if myAnswer7 == 1:
            result8 = a + 12.5
            break

        elif myAnswer7 == 2:
            result8 = a + 6.25
            break

        elif myAnswer7 == 3:
            result8 = a - 6.25
            break

        elif myAnswer7 == 4:
            result8 = a - 12.5
            break
        else:
            print("잘못입력했습니다.")
            break


    
    

    while True:    
        
        question8 = ("8.친구들과의 해외여행, 이럴 때 나의 역할은?")
        ques8Answer = {
        "1" : "친구들! 여행일정은 내게 맡기라구!", 
        "2" : "일정은 내가 준비할테니, 나머지를 부탁해", 
        "3" : "일단 비행기랑 숙소만 있으면 되지 뭐~ 그건 내가 할게", 
        "4" : "와!!! 여행이야?!! 너무 좋다!! (그저 좋다..)"
        }  

        print(ques8Answer)
        myAnswer9 = int(input("답변 : "))

        if myAnswer9 == 1:
            result10 = result8 + 12.5
            break

        elif myAnswer9 == 2:
            result10 = result8 + 6.25
            break
        elif myAnswer9 == 3:
            result10 = result8 - 6.25
            break

        elif myAnswer9 == 4:
            result10 = result8 - 12.5
            break
        else:
            print("잘못입력했습니다.")
            break

    if result8 > 50:
        return "J" , result8
    else :
        return "P" , result8

c,d= fourthclass(a)

print(c)
print(d)

mymbti=e+c

mbtiscore1 =f
mbtiscore2 = d

mbtilist = {mbtiscore1, mbtiscore2 }  # 한사람의 mbti 수치 (값)


