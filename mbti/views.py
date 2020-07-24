from django.shortcuts import render
from django.http import request, JsonResponse
import requests
from .models import inputClient, MbtiResult
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import string
import random


#Variable Initialize
page = 7    #질문페이지 번호
image_name_set_1 = []
page_url = 'mbti/q1.html' #질문페이지를 띄워줄 HTML URL 저장용 변수
name_t=""
gender_t=""
password_t=""
email_t=""

    #포켓몬 크롤링 URL

    # E vs I
    #로젤리아/두두/꼴깍몬/노고치
    #잠만보/셀러/나시/아르코
    #아라리/우츠동/아보/디그다
    #리자드/마임맨/메타몽/랄토스

    # S vs N
    #치코리타/플러시/아차모/지그제구리
    #팬텀/도치보구/춤추새/단데기
    #나옹/알통몬/파라섹트/강챙이
    #푸호꼬/목도리키텔/딱충이/근육몬

    # T vs F
    #슬리퍼/쥬래곤/럭키/성원숭
    #파오리/로파파/냄새꼬/푸크린
    #푸푸린/파치리스/맘복치/에브이
    #마릴리/야부엉/리아코/쥬쥬

    # J vs P
    #쥬피썬더/메가가디언/꼬지모/게을킹
    #랜턴/후딘/네이티오/마자용
    #시드라/캐터피/야돈/고라파덕
    #꾸꾸리/누오/라프라스/미뇽

#포켓몬 이미지 URL셋
#INDEX당 1개의 페이지의 보기갯수
image_url_set = [
                                                [
                        'https://namu.wiki/w/%EB%A1%9C%EC%A6%88%EB%A0%88%EC%9D%B4%EB%93%9C',
                        'https://namu.wiki/w/%EB%91%90%ED%8A%B8%EB%A6%AC%EC%98%A4',
                        'https://namu.wiki/w/%EA%BF%80%EA%BA%BD%EB%AA%AC',
                        'https://namu.wiki/w/%EB%85%B8%EA%B3%A0%EC%B9%98',

                        'https://namu.wiki/w/%EC%9E%A0%EB%A7%8C%EB%B3%B4',
                        'https://namu.wiki/w/%ED%8C%8C%EB%A5%B4%EC%85%80',
                        'https://namu.wiki/w/%EB%82%98%EC%8B%9C(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                        'https://namu.wiki/w/%EC%95%84%EB%A5%B4%EC%BD%94'
                        ],

                        [
                         'https://namu.wiki/w/%EB%82%98%EC%8B%9C(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                         'https://namu.wiki/w/%EC%9A%B0%EC%B8%A0%EB%B3%B4%ED%8A%B8',
                         'https://namu.wiki/w/%EC%95%84%EB%B3%B4%ED%81%AC',
                         'https://namu.wiki/w/%EB%8B%A5%ED%8A%B8%EB%A6%AC%EC%98%A4',

                         'https://pokemon.fandom.com/ko/wiki/%EB%A6%AC%EC%9E%90%EB%93%9C_(%ED%8F%AC%EC%BC%93%EB%AA%AC)',
                         'https://namu.wiki/w/%EB%A7%88%EC%9E%84%EB%A7%A8',
                         'https://namu.wiki/w/%EB%A9%94%ED%83%80%EB%AA%BD',
                         'https://namu.wiki/w/%EB%9E%84%ED%86%A0%EC%8A%A4'
                        ],
                        
                        [    
                        'https://namu.wiki/w/%EC%B9%98%EC%BD%94%EB%A6%AC%ED%83%80',
                        'https://namu.wiki/w/%ED%94%8C%EB%9F%AC%EC%8B%9C(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                        'https://namu.wiki/w/%EC%95%84%EC%B0%A8%EB%AA%A8',
                        'https://namu.wiki/w/%EC%A7%81%EA%B5%AC%EB%A6%AC',

                        'https://namu.wiki/w/%ED%8C%AC%ED%85%80(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                        'https://namu.wiki/w/%EB%B8%8C%EB%A6%AC%EA%B0%80%EB%A1%A0',
                        'https://namu.wiki/w/%EC%B6%A4%EC%B6%94%EC%83%88',
                        'https://namu.wiki/w/%EB%8B%A8%EB%8D%B0%EA%B8%B0',
                        ],

                        [
                         'https://namu.wiki/w/%EB%82%98%EC%98%B9',
                         'https://namu.wiki/w/%EA%B4%B4%EB%A0%A5%EB%AA%AC',
                         'https://namu.wiki/w/%ED%8C%8C%EB%9D%BC%EC%84%B9%ED%8A%B8',
                         'https://namu.wiki/w/%EA%B0%95%EC%B1%99%EC%9D%B4',

                         'https://namu.wiki/w/%EB%A7%88%ED%8F%AD%EC%8B%9C',
                         'https://namu.wiki/w/%EC%9D%BC%EB%A0%88%EB%8F%84%EB%A6%AC%EC%9E%90%EB%93%9C',
                         'https://namu.wiki/w/%EB%8F%85%EC%B9%A8%EB%B6%95',
                         'https://namu.wiki/w/%EA%B4%B4%EB%A0%A5%EB%AA%AC'
                        ],

                        [
                        'https://namu.wiki/w/%EC%8A%AC%EB%A6%AC%ED%8D%BC(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                        'https://namu.wiki/w/%EC%A5%AC%EB%A0%88%EA%B3%A4',
                        'https://namu.wiki/w/%EB%9F%AD%ED%82%A4(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                        'https://namu.wiki/w/%EC%84%B1%EC%9B%90%EC%88%AD',
     
                        'https://namu.wiki/w/%ED%8C%8C%EC%98%A4%EB%A6%AC',
                        'https://namu.wiki/w/%EB%A1%9C%ED%8C%8C%ED%8C%8C',
                        'https://namu.wiki/w/%EB%9D%BC%ED%94%8C%EB%A0%88%EC%8B%9C%EC%95%84(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                        'https://namu.wiki/w/%ED%91%B8%ED%81%AC%EB%A6%B0',
                        ],

                        [
                         'https://namu.wiki/w/%ED%91%B8%EB%A6%B0(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                         'https://namu.wiki/w/%ED%8C%8C%EC%B9%98%EB%A6%AC%EC%8A%A4',
                         'https://namu.wiki/w/%EB%A7%98%EB%B3%B5%EC%B9%98',
                         'https://namu.wiki/w/%EC%97%90%EB%B8%8C%EC%9D%B4',

                         'https://namu.wiki/w/%EB%A7%88%EB%A6%B4%EB%A6%AC',
                         'https://namu.wiki/w/%EC%95%BC%EB%B6%80%EC%97%89',
                         'https://namu.wiki/w/%EC%9E%A5%ED%81%AC%EB%A1%9C%EB%8B%A4%EC%9D%BC',
                         'https://namu.wiki/w/%EC%A5%AC%EB%A0%88%EA%B3%A4'
                        ],

                        [
                        'https://namu.wiki/w/%EC%A5%AC%ED%94%BC%EC%8D%AC%EB%8D%94',
                        'https://namu.wiki/w/%EA%B0%80%EB%94%94%EC%95%88',
                        'https://namu.wiki/w/%EA%BC%AC%EC%A7%80%EB%AA%A8',
                        'https://namu.wiki/w/%EA%B2%8C%EC%9D%84%ED%82%B9',

                        'https://namu.wiki/w/%EB%9E%9C%ED%84%B4(%ED%8F%AC%EC%BC%93%EB%AA%AC%EC%8A%A4%ED%84%B0)',
                        'https://namu.wiki/w/%ED%9B%84%EB%94%98',
                        'https://namu.wiki/w/%EB%84%A4%EC%9D%B4%ED%8B%B0%EC%98%A4',
                        'https://namu.wiki/w/%EB%A7%88%EC%9E%90%EC%9A%A9',
                        ],

                        [
                        'https://namu.wiki/w/%ED%82%B9%EB%93%9C%EB%9D%BC',
                        'https://namu.wiki/w/%EB%8B%A8%EB%8D%B0%EA%B8%B0',
                        'https://namu.wiki/w/%EC%95%BC%EB%8F%84%EB%9E%80',
                        'https://namu.wiki/w/%EA%B3%A8%EB%8D%95',

                        'https://namu.wiki/w/%EB%A7%98%EB%AA%A8%EA%BE%B8%EB%A6%AC',
                        'https://namu.wiki/w/%EB%88%84%EC%98%A4',
                        'https://namu.wiki/w/%EB%9D%BC%ED%94%84%EB%9D%BC%EC%8A%A4',
                        'https://namu.wiki/w/%EB%A7%9D%EB%82%98%EB%87%BD'
                        ]

                     ]

#포켓몬 이미지 이름셋
#INDEX당 1개의페이지의 보기
image_name_set =[
                      [
                        "//w.namu.la/s/865f13d4fbacfd3da6461565a2660ea022e5579f13e02de2e42a4ca02eba80e352d8626965f1dfb1b07d52efc9cb2eb11368385c7f54311f3b130b667408ad82b4069ae7936e176508550bd9b57c32aa2f13f701f5c6cc9f2f29daabbaa75c38",
                        "//w.namu.la/s/4d42f745d9c24b8b4edf3bd4b063f2a45a85a77686008d2cc7049f27e6366af70bc94ab99e0323e66614ea6a84174a023f76688c0497dd7174904042f5d1112bd3b48e5521b506d9963a24019f43f8e45aa683bd0a1e6168659dc70376c023c5",
                        "//w.namu.la/s/eba39f0a0dcdbccd07b3226c634d149a902d362ffdd91aed0bbece92a178ac698e2c83311709846c63a996bc355b8673da4e8236b81621a8e11400a4cd8f9f7129e2d4ba42f9a5e04648229ff215a457e9a06dbab61c5f47cc23e4f6cc6e1ca3",
                        "//ww.namu.la/s/8e6c96e009968af168ad6b4111c9f008d650f6fa0026f67c82a6a49204f95bdb83c279eb54ac8b74d2149732e80091ed21d672883ef18762ea12d74ef73ab62bed3051ac85cd4b32285d4c19b59af92fec74bb54f086353e5b23ecd697ed99f9",

                        "//w.namu.la/s/3c97f461717d389f533f48b9c1b423c16b3eda3021a0c3468ff6c1d784d1efddc83e916ebedf6d4cd94f89f41613e350c062f3c8443acdb62a8ee4d2fdcb177b7d34c8c2871186bf07aee21369863d5c84986ca4d84e0ff4a7bd8772e3fde310",
                        "//w.namu.la/s/fb597bfe9cd80edbc24a4f327253e6bb045f85a53886e2ee866ec70d15dd14fe52b8b6dac07a308c6fe39e5ed013ea2520bb042f9ca77b6dc79ed3961b8a00835f481684316dca5a31c405971819a464754d65caeec469bf5ea206587fed8bb2",
                        "//ww.namu.la/s/4735e3dce016ad32657cee84b003ecd3e9c3eb1bd983de124f750c6f8341726a90dd693ea82e5274c21032cebf8302156c29ab72687bb9723232bc58222987ce3df18fd887dab5a6d6d9f8242094eb7dfd8714b8a151e0f56bd5445f9b61ff2f",
                        "//w.namu.la/s/2baf7cc510ffa3c694cb783bc0b16a7751f676b496046a81cd03e30f338216d53e7b1d93b80f232dd4b555e26c0eacbf29adea38a6011dabed5d7cdbd16daa79572666f162469247cc0f445712ffa0e0412d270186bddb2b23a8977272032be7"
                      ],

                      [
                          "//ww.namu.la/s/f24ac2625a99a906fecc37c7b5d2512ce2b88eb1bf688d48d2896cab182fdc712b6755fc4f4e93488079456ac3383dbe29e8432e5585f5d7a727ceca30917e044e832624a58c2908b5800f3f368e7a8998d38b82d1a59991c6448793bdc222e0",
                          "//w.namu.la/s/560ecfc7a90ea2339a978e023a51813f2531101d29033d6e702ca37391070383d0220bd8b70b9d8377672a4ede36528a20c081d3941bf1204a647941fdcd1d0434ec2a3693c876901ffd2864d7539ef95bd4b64cbabd6c0cbe7af4d1b24fa7d3",
                          "//ww.namu.la/s/d89328c92c5efce14394a33c7c1237bede979bbd19fa510e44ac370db188ce101b93417816bca32f45e8b0c200f66cca99f8475c6e05210c633404434041d1cc94abfa910f3307f4c65c391a4ad8ed5d87036adaa87fd2d84d9543963ae5a8ec",
                          "//ww.namu.la/s/7d93b5bf491582266eea375fcae3138b83a7e722c89c98be06a4f736d504c95ae25971fb88eff3c5cceff501ec98fb2f8ae7ee604ff17013bf7b50c7a7d23f6119cb95614b51359cc4f5f284179b7b31c98628cc09f11b7ed5865792ccb52ca6",

                          "//vignette.wikia.nocookie.net/pokemon/images/8/8a/%EB%8F%84%ED%8A%B8_5%EB%B8%94%ED%99%942_005.gif/revision/latest?cb=20120902080152&path-prefix=ko",
                          "//ww.namu.la/s/313e7873b7d058134d167c7a7c18d43b2972a31c21fadd18fae3a37477ae4c335b2691b9d6eb076c08343cabf941f03a54f8e9ca0f16aa715c33419f66af4ead0303d907eaf5667a80ca5dff599b3510e2553aa523ee57d0fc37453427a9d246",
                          "//ww.namu.la/s/dcede70cc2c69d440138a5f3e36718ca15db27ba18fe324acf3743273c2f8c6a405f85d24c8b4fc4cf57f13ac65a9ba79609f0544ada705b7ac7b5706da6b5cb39f60e1dd84ae92243040a6c0567fa0f5801eb7c6a6d489cdaee44d9e63b3658",
                          "//ww.namu.la/s/d519324ae53183aaf766bff34b71d8fc316a05df98cae5774507d3878ad8f7653e900c55c6b9d667091e923ec42c28feafc0f15a3c483d71856d374b65bb6a514b184c273d647794eb30c9322099ac192b89e0fe7f3457444a48ece20d095c59"
                      ],
                      

                      [
                        "//ww.namu.la/s/77f8b89db4cc053203831f8b2149f0ef387941b66be69dc277ea3a3db40927898e62e8131d269ff5a00f25dffad44452b37fb473b2cda5d278111e5ac909bb67da36bd9653a3ee649ba20baefb35bba596e035b67f63fe3cfabd1f5985c729e3",
                        "//ww.namu.la/s/d6c0016689a07adba56338888310ce09f41b3fdc96ef0e3075b3fa75181e01f9464faa273b622b420915d1537caf07f301b8489ae2dbfedd407e03e3c33db5175432508b6269b035117a2e1216eae97f71d0a0ecd5df6850b3ada3bdf31de36b",
                        "//ww.namu.la/s/4748ebfd87c4f48f67b34384dc6161211f8222b0db95cccaa3bdcd1d768acb3e8814f286cd6cb5237697d43e150534f8d08bd185b4ee4fe6ea52a81163aa0e6840c7f4406392536d4e0c337c16d8aeb22e8e23c26bf92583f658d5ed239dcce9",
                        "//ww.namu.la/s/cdb3e0f1bbfb2a59cca88dbfd98931d3b085f9c7df89292cba5729828b342fe46aa338107c7a49c92c2f578339b3ba57232ac144f21a171e8e9211a4e58685c2446d39ac5aa03ae3c43c470481040ca6dcebb2a70a1c33c3dabe4982ed330db4",
  
                        "//w.namu.la/s/2c740e11b22b2a62a2d53d70f727bec9022e1e36994d5bf22da1c95676dff2803ad5e01933da1af08e38b5c117e5c3f95355a3f4e093a276a2f678400595d9751cc86f5fb02b30d979dff773c12ce4134e44d9b46526e066a05531cb507deaaf",
                        "//w.namu.la/s/eba4c13c1896fe8e72ef60f2b3a7d0bd59f62edafe605d766ce00cb7adad54ff788c531c45f08560eed48723e57d07815eb769c123f039626f7ab9ce154938ac98fa34138744ba00a21facd681229c7e21b56edb43554827506bb9c59b41ff67",
                        "//w.namu.la/s/698d2f2430545589aa318c37cb2d4eebd99166e054e5a7640736dabf8c547f0df9fc1280a36c3e2796a384cee1d8924c07bde4cca8502a7c083abcf3e59da37e07d06ae41c6a6b096a66d6bcfe628a767a0ab75425755b8c410e56ea7dc2502c",
                        "//w.namu.la/s/69e9cc9077e13eb826ce9745e62805770d37476c155ba932a6cd3b4d9be643eba67691e794192d534278ba05676de30e3dc56061532b0c25fbc00ceb880f9926139088601b533e11874c1c4bf4102f8aca164227bfc0017c0f0f1c6ff570c7d4",
                      ],

                      [
                       "//ww.namu.la/s/8bde3f75617a54050a9600dd9efb9afac69dbc96a2dde12028f493f94218b4d7debca2e0adbaa8c81ee2db0a1893c87f9d151eefd1aba7aec1641f59ada3d7919ce600b3c3e4149a21427d50394d95915b8d4cce84dfb23be55928f1a583dc4b",
                       "//ww.namu.la/s/a55745c24f00897b163b27e036c02921074648455ae6921222f5b5fb26a1b3f068c3ab9fe5efb05cffbee9081606136501cc4c4674d385f545340d3005c841b7b8cb6629a817a2644877af288abdb821d40e39412aaf941f29678cfcd0442649",
                       "//w.namu.la/s/af6bbddc56dd50a9142667f2acd25c815b162ea88b85183b2c7c6fd64e676db614b3841bc63ea538659449c7627dc884c775f1c49607bdb972ecc4d6796bcbfd586ea441afbc437d01e25d6def30f3665383382e50ecd76555fe3cb1db536424",
                       "//ww.namu.la/s/10ef05f284585f6544387dbc016906cdae6bb018433345e4106c7e2c8aeb63989ec6109a8ddf6828282e452b106786e50f16b78ccb66cff2a60a3a5dd14f51b969f6822cf6db9a9e9a10a3355c9f3c2052f7859218e09b7d3196b5c3149a6486",
                       
                       "//ww.namu.la/s/924cd5d4a587fa80ab8fca6e27fa4c170e061ae09fb6942df11f12a392a33b8106603fbee1b9d235d88449d8f4a7a7f40a07790f8378d3ae9e19900846b8d35f254cde63d4a1b97c3dbeb338875c3ced902addb7dbfc2f74b1ee9f242bedc15a",
                       "//w.namu.la/s/1f487786094dad450bf06ef75cdcd8e33d3f890005a04802e390f75ed2e81435304c2ca0016f8f9ab5ece8fa517966ebf01d85f838b3a0613c1d85de0aca34054f1e996621a4a149e7d6cc7b99e83fe249d2926be72decaa2c1360398a22d861",
                       "//ww.namu.la/s/792c6997488db006edf5744efe3a6a6fd7838f15b41197920e71185de1180df2d8025e7275368278f30a61118dda4b808006a0c16b18a41d616731d8be3060ccc15c17f74daaaf955314667939f4dcbf44a1a9fd02185de55dca3f056879c5db",
                       "//w.namu.la/s/e7b5b715775a38258adb2815b29cdbbd9edcedaea87edd7309831be02b364853afc786831dcc0f4b521a7099e6595821cfc460fe59456ac53974eca7845fa36d2028f54dba013f35c0b4a34701b1d68da819c277104c1739da11967af15ed9af"
                      ],

                      [
                      "//ww.namu.la/s/4b11cb4c3146630445791da96274073b380b9c7364d8cb294a2c5cfdcb9f573ebc61a7c4a6f5c33384dff98e7db252469a18afc2091534a03269e5c3bc3610ac7b873b4ab8e8b97756f42ee66cd8033fce2831f5e3e111700328a0d1d0598c44",
                      "//ww.namu.la/s/0a8bd2b433374d15ebbdad1f6260310db8f8af68609cd937aa729a44a04df7c2dd344559b1b2e292dd2c3ecf3ff5519cbcad408f371e89c635f55ecd34e50b149c877151bc3ecd9fbfbcb102b8573c718e592f6b1fe9c2ceabbdcaf01e467b32",
                      "//w.namu.la/s/79de51b5845c51780466d5bc20bdcd1bfc6cec7ab183beaaf3ce109a875b4df4d26a2dcbfe3f18b443725d63b2b614833c68711b98d2c6349574c77738d206df958b1ff3acb0cafd256339dee2643668070d3bc05a88fa11a0e6960fd4c6211d",
                      "//ww.namu.la/s/382631b3d4f11720fbe8bbf1ab13941cc909306a4d0663492b9d3b1452a9c3f8b023225c7d7d80b9a31a1e0ef7a1f6c4ee7d69a056365724be39d637c31c2a1ff152692e7ea7776d5415eda4b0a65c30e5865b800064bfa4dd528e8eb25279ea",

                      "//ww.namu.la/s/2206e6d3ce7fb58e2c4ac26008b5a82d4cb153f653cca8410e0b006290cc4a6cd06421b3166098e664e22966d3556a21c4d859f1479eec31836bd7fec22820f3acebc924b1236644d404143070ee7cd1b2d436abcc978a31ecb6e34efca246bc",
                      "//w.namu.la/s/9c813f1ff45deb070cd86fc9d7228535b754c4b30464558969751b13b2ecc7f673b3511105bacc5dd2a12c1ac08d8d0d3891eba6b04253c4d1ac59349e6b20859855f887edb3c5e46ff47696b6944ddfcf567744e70aa3c01018d5e70e0193da",
                      "//w.namu.la/s/220d02329602c6f6c2f1d21c5a0c9946bd4b6cafeb628a2c53d9cd8f9744ad372c7aea90ceda4bc0507ef10ed0360ee968e12f287583e7eee14336405a2674027375f00697bc354c5706293d6a02481353f23eaae0f06669fedcacff2621c00d",
                      "//ww.namu.la/s/345ea1e364b22979e679549aa5ca785d3432116e6de9a0c225c726a6af4b679c20309c0ee2af84cd55fa205f31a6c105cb045391df3508d4ffb226e371bd8d7773e99b37f9f14e973986bc0aa65609e9659bdaad4fa2b120ab7f1069d56d8372",
                      ],

                      [
                       "//ww.namu.la/s/4c3006d30fddbbfcfd54165ffc9223016fd7e0374295372097a7f071bc4ad49d23ef676c0e8bcacf68f2e5265153d788572e5d137d21788dbb134020b52f13f297d7492b7da1d126a6a42d19ac3b55ccfd81000139ccedd52b0361dc806ded8b",
                       "//ww.namu.la/s/bf3579af15bd246460b5da47f6da1d8b94eae36b7a53aaacd82ac37465c7e0265e045be838938b1a298df45b45d5507c9733028f4c65155b320fe4cbd88a5bbd26ce00d764347e7ce29e74dd95f903bcf562774b1fa8d75979f16827db9baf36",
                       "//ww.namu.la/s/e677ecce68fa6b34d1ea1a7e98630e0ab0f0cef5f7a93a342ae51da834d0665d8c829accaf9ec5b75f656943887e919a7740858ae341aee4c84cee7e791652d551714669b00ac8d03e3f589027bd2247a54ce03d1a9ef370dcf7331444b5a2d9",
                       "//w.namu.la/s/299bfd1da53dcbb022ccd666d2d54fa11d36d1ce0b7064c9200f124514b0d6770154d21b4680da839ca176b5fe6904c8053eed614eb50eca0276e989a24e2a6b7b1300e0b85e9ed628c42ddb1ffef5083245e55451e9a6ec2a855df7f95d7614",

                       "//ww.namu.la/s/808d66bb69740f5f9ffa318f53b205ac6f80dc3cfdb49c2265ef7a1c72d518d9af4b307c5021f5c6e56f4d9a726cb30a2604e22c030bf971ab9acbbc8cb86675ffaa825e7d6068e437c4789dced4abf478044916141741d00b3327f25f8462db",
                       "//ww.namu.la/s/266fd3279b9e7e1613f0e0a26f579b76e648a10d9a3132511a9d338623cb7a7721355d5b1760202961b9befbbfe2f7bae9b2cbd4266508125d31504fcde83e4d4719aaf1cc4d140e52db416dedb50cd74e16d73c7a09a842b5e7707431c5226c",
                       "//w.namu.la/s/fe933c25ae52c21005c036ab016275c6f00ba0402a8151ae57d3797acbcc615e369a47281dd41e3563a86714117f7f4ccf22efd49058db3ad31d31720e119ba9f0d48be5bff9a05d276bd7cc738b01c42444956973b0ee061bc9f9de613f31ad",
                       "//w.namu.la/s/d90e2abe987913e036ebae30ba6cb3010a5f9816e14eec38a8188d10fad9fce32ec1c0a50732747908c65622868f3364ab156154cca1e8fb6c1d9aa2331b7e533cd00f74855062a81b48a34a50eb53baf0ebb331d22cfac65cab88af56220e83"
                      ],

                      [
                        "//w.namu.la/s/c13c205939d5fec6dbb543914402837acc0a400d4d0eb32a6b5e8d9a222cfe4052f12230d6d8e8f0c8768c26130ae1093163acecc6c27561a7e8ae94be96e98b80fcca5b3a4ffb592156e18f3681dfb5ad9c700d3b11e41cd0814d77330f25c0",
                        "//ww.namu.la/s/6bd60742ef6fe6d5425f830c4b73d1e36269be05528c6e409f3790645ea710d320124a72fb4f29fa706402b6907ffde1b4b72341c7612747833377e746d0a8345f5fb05a3362ed0d171fa09c9c9033f43ebd57708f565ec388a6c02cfb70ca39",
                        "//ww.namu.la/s/36a1e7828d2fd125bc86c47aa526751fb02719900de23e86700487786563e6c6a927db56521777f307ba7727e7713c3e0c356f7f189be57b42b89ee44f3a7222f38c411685775f1f90273be46a3b9084126d6825bd9b663d0ee1ba090d651624",
                        "//w.namu.la/s/585cc0255ea64aeba46b8fcc4924a11f6629d7f5a93e4297613271956ce6ac58ca5b8c2a83e35bcda3e1fa6d69f9126f0cd5ad0d7471329a498936017901e7176bb1f72bd586e5f65a50a3829de4fc8ada903eee5593c86f1a5f84744ddffeb6",
 
                        "//ww.namu.la/s/919533d8ecbae591757118f1874e370031e617ee1d252d91f4778470d433ba30578d33402edcdc524aa66dafc34781aaf824040f064fbc491b8b9ab4c9a000a8bbcf75ad64b0759579a66717e7b8c582ea5d6a9e675c9daa70ac4224fa221455",
                        "//w.namu.la/s/a25d80ecad64fb37abd69c03222ab5d10416001349e15a9fd0fc4380de623b3876174614ae6928a654855ca01355f3859d537a6a3251c8791551a74bcb40c3967b68b84ba75d15ba29c1cb826a4d0a4b2afacb80c4ba31d982e3ad3950f269ac",
                        "//ww.namu.la/s/16a33404f9c5eec4b861995870df9cf3747f11fc4f4d0ff8bfd8d97de255e93347bb4c0f8e4fab482535d118c85c01ee2e5cbc0663a2bb5f625c306716f3ede380979c5474764c48e7ea23172e14bb488dcccc4e02c6ce9b97a2234cb05baa5c",
                        "//ww.namu.la/s/e64781c497971f9416fe5711450bd66d10bfa2a05fbb2409e451e12ae70fad29e86b21c34ab8784a17f12d885edcf430ea46f0a918cf9f86a66027812303e70cb723b70ddf091195d739d4c61cddfbc336fff1fe87aee4e1d3b3c3b13d6e73ed",
                      ],

                      [
                        "//ww.namu.la/s/3dcc8ab5dd63d2177ad7a4225eb1c815cab3471aa8f19087963d9822ca048f18b2cdb282d7646326aeb01fdc4bc1112a08aecbeef5aaaf74fd36609038d6cb48b9c5d54ee9d7c4151c414ce30af7114ed4a55eac3c8afbacc4adc59cc9ae9e76",
                        "//ww.namu.la/s/2aa1986f6374d16a0342a89d71bff0ddb1f655b99c2285b06c43370b4180d405116ad9ec2ceedc3c7622f55ec9c6cffd2a8d9a38b4e8783588c0fd03323f8f18c7e15dc7b7f45aec14b9af653f61ffe0a4860db408ba95193ccbe7efc8b4d46f",
                        "//w.namu.la/s/5a0493cc6b96817b4a89c4dfc1f1d18b747a0e432c9ab02d4d89c99bff3e554a7818700d71a947bfba6c1db07d92092d143c6a7e5228583461cf5fbbc0d1efd88cce6514bdec2e89d018880ff1c2afb673f00f3907f2c79652d055299281d298",
                        "//w.namu.la/s/10b61617f36f154119333046472f960078ff6d50d1c7e2073511316d0501f140ff019582b62dd728d7606e4e35ce0d5fe037f3ed1d34743fdc6287f062013ad3b5dab1bc8f85ef95aade7b5494b91a7802bcf5c1efb2ddfffb0337e34edd5c7a",
                        
                        "//w.namu.la/s/068e055090f343a7c1e2191ce6b9857280645a36904d64264afeeb1bcada65807b95e981c922171355d786138d2c88f0181c9dca285701c446eba5afcb6bfbc1552f1eada03b61ff12271366a58383a8812e9b9e2ad9577096a93485238de44f",
                        "//w.namu.la/s/a1740b30cb56ac370d4c784e4cfaf210a450070fceeed1dbb6e3925ee62c63622a9bde67a55d3324fb8e2ad0b187cc828b16a0e0dbedb1950d4981eb3120a18546782301c8d50b3930b7d3713af11d4ac992d12defa6f1328c7f1063d85d8bb7",
                        "//ww.namu.la/s/51cb53d869858b1d78ed3e50c7e9bf75887156f430afa621af518195650c38aaf678af070042f29b0367c5056646a9be4ae527036116e3beefc0ccfd68edd53e1a676ef3759bbfb698c42b947b10a4f142915cc539cf2ae646e0470f5243d076",
                        "//w.namu.la/s/8473a6cb368acf2ba19720fdd51188ece725c90af097fa2a51224e06670fd66ebad396bcd5f2cdc3a333e2c195f616d0896249487b5aec46cd4af6ae0559987e52a2c54d7813595615e4a7a7582435a7bede053a7edea42122b527dd75e500ff"
                      ]  

                ]

# #MBTI 검사 결과

#0 ISTJ : 홍수몬
#1 ISTP : 루카리오
#2 ISFJ : 망나뇽
#3 ISFP : 메가파비코리
#4 INTJ : 엔테이
#5 INTP : 레어코일
#6 INFJ : 메가후딘
#7 INFP : 뮤
#8 ESTJ : 샤미드
#9 ESTP : 뽀뽀라 
#10 ESFJ : 해피너스
#11 ESFP : 피카츄
#12 ENTJ : 메가거북왕
#13 ENTP : 기기어르
#14 ENFJ : 로즈레이드
#15 ENFP: 파이숭이

result_image_set1 = [
    '//post-phinf.pstatic.net/MjAxODA0MDNfMTU2/MDAxNTIyNjg4Njk2MTY4.Mvyj9N6ANc3uAgVTO1dDT3leClH_zE2pkkMgWeY-Unwg.D5gKckpYVGiNYM3cNRrxVFvbm73iUJT7BF0BfTizJ9sg.GIF/%EC%9E%AC%ED%82%A4%EC%B0%AC2.gif?type=w1200',
    '//45.media.tumblr.com/d2c36aed16916b433c523de756c7f613/tumblr_n72p1ngmyw1rpn9eno1_500.gif',
    '//t1.daumcdn.net/cfile/tistory/223F724E57E5BA5319',
    '//blogfiles.pstatic.net/MjAxOTAyMTdfMjkx/MDAxNTUwNDEyMjUxNjIx.rAPl_fGZQfTGJ6JWQWiIy3Jm5F06racZ5fGGowTb93Qg.1wQUKqyZwtKRz5nirjJW59wjkc1A_m1UoSEsUUf0hbcg.GIF.unesco1128/19.gif?type=w2',
    '//post-phinf.pstatic.net/MjAxODA5MTRfMjEz/MDAxNTM2ODg3NzM3MzAx.YLeRemJ8sX8VYMd8cNw5zbpkBxUMn6qPSlRBxMVssaEg.Ro3OwdOGTX6quxroguBIMkvloKgtGniqP9tHREvf3tsg.GIF/%EC%95%A4%ED%85%8C%EC%9D%B4.gif?type=w1200',
    '//postfiles.pstatic.net/MjAxODA5MjdfNDkg/MDAxNTM3OTc3MjYzMjIy.J1H5D1v8e2nXuyp__l_K79lSKQ0IEesZ3xFEpqqDKQ8g.DGFmZ6gF_6m2ewS53qZ5nzOA6yj6KrFOOgFzvDK49qMg.GIF.lcj1222/f92b9fa247937eadd4a3dea8656c5f3d33f7aed7_hq.gif?type=w966',
    '//upload2.inven.co.kr/upload/2017/08/17/bbs/i16690725871.gif',
    '//t1.daumcdn.net/cfile/tistory/9942BC3C5ADC889403',

    '//1.gall-gif.com/hygall/files/attach/images/82/754/913/187/9f633675734c20042e1a2cba5c27d260.gif',
    '//img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile2.uf.tistory.com%2Fimage%2F99078C395ADC88F00AA639',
    '//img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile24.uf.tistory.com%2Fimage%2F99F65A375ADC88FF22FAD4',
    '//m.dragonvillage.net/assets/data/board/humor/2017_03_01/20170301_b8c358bf9743ab592ef7fb03f0606a13/2317895460_1488345287468103.gif',
    '//t1.daumcdn.net/cfile/tistory/262AF65057E5BA621D',
    '//mblogthumb-phinf.pstatic.net/MjAxOTA4MjJfMjM0/MDAxNTY2NDY4MDk5MzU2.15E2JzL9RyWz3oA8tI1lRVhGW8DxXTbm6y_jJh-MnIgg.G8p5phrs2iOu93kRuFY4NXtgUuIdOe83HI0TAA1iv6Ig.GIF.lcj1222/tumblr_nuzeu64SbF1sr6y44o3_500.gif?type=w800',
    '//t1.daumcdn.net/cfile/tistory/992BB43C5AE797231A',
    '//mblogthumb-phinf.pstatic.net/MjAxODAzMDJfNjEg/MDAxNTE5OTc5NjIyNTc0.WBSXHZCqZmrNXLRcia_9zOnQztVpmkJfKimpW4m2MlMg.dEY1tOneJeSrNC4bqSqHVOm8Z3TVEVKll11PNiTc0skg.GIF.lcj1222/giphy_%2815%29.gif?type=w800',
]
result_text_set = [
    '1000승을 목표로 달리는 홍수몬(ISTJ)' ,
    '뛰어난 적응력, 논리적으로 사고하는 루카리오(ISTP)',
    '성실하고 온화한 망나뇽(ISFJ)',
    '나보다 남을 먼저 ! 메가파비코리(ISFP)',
    '비전을 제시하여 나아가는 엔테이(INTJ)',
    '남다른 시선과 아이디어를 가진 레어코일(INTP)',
    '모든 것을 꿰뚫어 보는 메가후딘(INFJ)',
    '유토피아를 꿈꾸는 뮤(INFP)',

    '팩트 중심! 실용 중심! 사업가 샤미드(ESTJ)',
    '혼자보다 함께! 다양함을 선호하는 뽀뽀라(ESTP)',
    '친절하고 봉사정신으로 똘똘뭉친 해피너스(ESFJ)',
    '누구와도 분위기를 고조시키는 인싸 피카츄(ESFP)',
    '비전을 향해 동료에게 힘을 불어 넣는 메가거북왕(ENTJ)',
    '풍부한 상상력을 가지고 새로운 것을 창조하려는 기기어르(ENTP)',
    '언변능숙! 서번트리더십을 가진 로즈레이드(ENFJ)',
    '항상 열정적으로 새로운 관계를 만드는 파이숭이(ENFP)',
]

result_text_set1 = [
    '특징 : 철저하고 건실하고 체계적이며 세부적인 사항과 절차에 철저합니다. 이 성격의 소유자들은 절대로 충동적으로 무슨 일에 뛰어들지 않습니다. 하지만 한번 시작하면 중단하거나 단념하지 않습니다. 반복적인 일을 싫증 내지 않고 잘 처리해 나갑니다.',
    '특징 : 이 성격의 소유자는 책임감이 강하고 온화하며 헌신적입니다. 또한 현실적이고 실용적이며 꼼꼼하여, 치밀함과 반복을 요구하는 일에 능합니다. 그로 인해 일처리에서도 현실감각을 가지고 있으며 실제적이고 조직적으로 잘 처리해 나갑니다. ',
    '특징 : 이 성격 유형은 창의력과 통찰력이 뛰어난 사람입니다. 직관력이 풍부해 뛰어난 영감으로 타인에게 영향력을 미칩니다. 또한 독창성이 풍부하고 독립심이 강해 확고한 신념과 뚜렷한 원칙을 가지고 삽니다. 무엇보다 공통의 이익을 위해 헌신하며 인화와 동료애를 중시합니다. 따라서 존경하며 따르는 사람이 많습니다.',
    '특징 : 이 성격 유형은 행동과 사고가 독창적입니다. 비전과 신념이 강해 독립적이고 단호하며 고집이 셉니다. 자신의 영감과 목적을 실현하려는 의지와 결단력이 강하여 직감과 통찰이 요구되는 일에서 능력을 발휘합니다. 복잡한 문제를 다루기를 좋아하며, 자기가 관심을 가진 일이라면 조직력을 발휘하여 추진하는 힘이 있습니다.',
    '특징 : 이 성격의 소유자들은 조용하고 말이 없으며 논리적이고 분석적입니다. 그리고 현실 감각이 뛰어나고 임기응변에 강하여 일을 능숙하게 잘 해냅니다. 자신과 관계되지 않은 상황이나 사람들 일에 뛰어들지 않는 경향이 있어 가까운 친구들 외에는 사람들과 사귀지 않는 편입니다.',
    '특징 : 이 성격의 소유자들은 마음이 따뜻하고 온정적인 사람입니다. 따뜻함을 말보다는 행동으로 나타내며 조용하고 신중합니다. 6가지 성격 유형 중 가장 겸손한 유형이지만 상대방을 잘 알기 전까지는 이것을 잘 드러내지 않는 특징을 가지고 있습니다. 또한 자연, 사물 그리고 예술 등을 감상하는 능력과 식별력이 뛰어나며 동물 애호가가 많습니다.',
    '특징 : 이 성격의 소유자들은 마음이 따뜻한 사람이나 상대방을 잘 알기 전까지는 잘 표현하지 않습니다. 조용하고 자신과 관련되는 사람이나 일에 책임감이 강하고 자신이 추구하는 이상에 대해서는 뜨겁고 정열적인 신념을 가지고 있습니다. 그러나 내적 신념이 위협받는 상황에서는 조금도 양보하지 않으며 남을 지배하거나 좋은 인상을 주려는 경향은 나타나지 않습니다.',
    '특징 : 이 성격의 소유자들은 조용하고 과묵하나 자기가 관심 가진 분야에 대해서는 말을 잘합니다. 무엇보다 사람을 중시하기보다 아이디어에 관심이 많아 분석적이고 논리적이며 객관적입니다. 따라서 이해가 빠르고 직관력과 통찰력이 있어 재능이 많고 지적 관심이 많습니다.',

    '특징 : 이 성격의 소유자는 자신에게 일어나는 일에 대해 개방적이기 때문에 사물이나 사람에 대해 선입견이나 편견을 가지고 대하지 않습니다. 관대하고 느긋하며 우호적이고 관용적이어서 적응을 잘합니다. 규범에 얽매이기 보다는 현재 상황에 맞추어 나가는 것을 선호합니다. ',

    '특징: 이 성격의 소유자는 사람에대한 호기심이 많고 다른 사람의 말에 잘 끼여들며 참견을 잘합니다. 이론이나 책을 통해 배우기보다는 경험이나 실생활을 통해 배우는 것을 좋아합니다. 그로 인해 추상적 관념이나 이론보다 구체적 사실들을 잘 기억합니다. ',
    '특징: 이 성격의 소유자들은 풍부한 상상력을 가지고 새로운 일을 잘 시작합니다. 무엇보다 충동적인 에너지를 가지고 재빠르게 해결하며 솔선수범합니다. 또한 관심있는 일이면 무엇이든지 해내는 열성파이며, 뛰어난 통찰력으로 상대방안에 있는 성장·발전할 수 있는 가능성을 들여다봅니다.',
    '특징: 이 성격의 소유자들은 안목이 넓고 다방면에 재주가 있으며 자신감이 많습니다. 사람들의 동향에 민감하고 민첩하며 여러 가지 일에 재능을 발휘합니다. 또한 복잡한 문제를 잘 해결하고 정력적인 에너지를 가지고 있으며, 부단히 새로운 일을 찾아 나서며 시작하는 가운데서 끊임없이 에너지를 충전 받습니다.',
    '특징 : 이 성격의 가장 큰 장점은 일을 잘 처리하는 것입니다. 일을 계획하고 추진하는데 뛰어난 능력을 가지고 있습니다. 현실적이고 체계적이며 논리적이어서, 일이나 속해 있는 집단을 잘 이끌어 갑니다. 규칙과 규범을 중시하고 어떤 일을 진행할 때 확고한 사실과 정보에 바탕을 두고 움직입니다. 따라서 미래의 가능성보다는 현재의 사실을 더 중시하는 경향이 있습니다.',
    '특징: 이 성격의 소유자는 자기 주변 사람들에게 관심이 많고 우호적이며 화목과 친목을 중시합니다. 또한 양심적이고 정리정돈을 잘하며, 사람들을 잘 돕는 특징이 있습니다. 그로 인해 주위 사람들을 인정하고 지지해줄 때 기쁨과 만족을 느끼며, 자기 자신의 판단보다 주위 사람의 인정이 더 중요합니다.',
    '특징 : 이 성격의 소유자는 동정심이 많고 민첩, 성실하고 참을성이 많습니다. 상대방의 의견을 존중하고 새로운 아이디어와 일에 관심이 많습니다. 글로 쓰기 보다는 말과 행동으로 나타내기를 좋아합니다. 또한 다른 사람으로부터의 인정을 중시합니다. 하지만 다른 사람의 장점을 발견하면 이를 지나치게 이상화시켜 맹목적인 경향을 나타냅니다.',    
    '특징 : 이 성격의 소유자는 사전에 철저한 준비를 하여 조직적이고 체계적으로 일을 추진합니다. 비능률적이고 불확실한 일에는 관심을 나타내지 않습니다. 새로운 지식, 아이디어에 관심이 많으며 솔직하고 통솔력이 있습니다. 즉, 어디에서든지 목표를 위해 사람들을 조직하는 일에 능통합니다.',
]

result_text_set2 = [
    '대인관계: 가족이나 친구관계에서 신뢰할 수 있고 헌신적입니다. 즉 부모와 같이 다른 사람까지 책임지려는 경향이 있습니다. 차분하고 논리적이며 판단력이 좋습니다. 하지만 다른 사람들도 자신과 같다고 생각하여 그들에 대한 적절하지 못한 판단을 내려버리거나 감정을 무시하는 경우가 있습니다.',
    '대인관계: 전적으로 신뢰할 수 있는 사람입니다. 상사에게 충성하고 조직보다 개인을 더 의식하여, 상사를 비롯해 다른 사람을 존중하고 절차를 따릅니다. 또한 잘난체하는 것을 싫어하며, 겸손하고 조용한 친구를 좋아합니다. 또한 의사소통에 있어서 솔직하고 핵심적이며, 실례나 견본을 사용합니다.',
    '대인관계: 타인을 기쁘게 해주는 것을 좋아하며 어떠한 경우에도 최선을 다합니다. 무엇보다 갈등상황을 싫어하고 파괴적이라 생각하며, 다른 사람의 말에 귀를 기울이며 기꺼이 상의하고 협조합니다. 그로인해 타인에 동의하는 쪽을 택하기도 합니다.',
    '대인관계 : 다른 사람의 말에 별로 영향을 받지 않습니다. 특정한 대상에게 쏟는 정이 유별나지만 나머지에게는 냉랭합니다. 정서표현하는 것을 어려워하고, 자신이 관심이 있는 사람들로부터 거부당했을 때 가장 과민한 반응을 보입니다. 독립하려는 욕구가 가장 강하고 사생활을 보장받고자 하는 욕구도 강합니다.',
    '대인관계 : 열정적이지만 조용하고 호기심이 많으며, 사람을 사귈 때 친한 친구들을 제외하고는 수줍어 하는 편입니다. 사고능력이 뛰어나기는 하지만 잘 표현을 하지 않습니다. 그러나 자신들이 흥미를 가지는 분야에 대해서는 놀랄 만큼 이야기를 잘합니다.',
    '대인관계: 점잖고 이해성이 많으며 불행한 사람에게는 동정적입니다. 조용하고 겸손하며 수줍어하는 모습이 대화로 나타나기도 하지만 일단 나서면 "무대체질"을 발휘하여 주위 사람을 놀래 키기도 합니다. 또한 대화에서 품위 있고 유모어를 즐기며 인간관계를 유지하고자 하는 욕구가 강합니다.',
    '대인관계: 외부에 침착하고 만족스러운 얼굴을 나타내며 과묵하고 수줍은 듯이 보입니다. 타인에 대해 냉랭한 것처럼 보이지만, 내면적으로는 결코 멀리하지 않습니다. 다른 유형에 보기 드문 것으로 특별한 사람들이나 어떤 하나의 명분을 깊고 열정적으로 돌보는 능력을 갖고 있습니다.',
    '대인 관계 : 다른 사람의 말에 별로 영향을 받지 않습니다. 특정한 대상에게 쏟는 정이 유별나지만 나머지에게는 냉랭합니다. 정서표현하는 것을 어려워하고, 자신이 관심이 있는 사람들로부터 거부당했을 때 가장 과민한 반응을 보입니다.독립하려는 욕구가 가장 강하고 사생활을 보장받고자 하는 욕구도 강합니다.',


    '대인관계 : 타인의 의도나 동기를 잘 추리해 내는데 재주가 있습니다. 말로 표현되지 않는 미세한 것 까지 감지할 수 있습니다. 재치있고 영리하며 사람들에게 재미와 웃음을 선사합니다. 반면에 불안이나 근심을 받아들이는 수용력은 약합니다. 따라서 인간관계에서 생기는 불화를 피하기 위해 마음 깊이 사람들과 사귀는 편은 아닙니다.',
    '대인관계: 홀로 있기를 피하고, 언제든지 남과 함께 하고자 합니다. 그래서 손쉽게 친구를 사귀며 사람들과 함께 하는 것을 좋아합니다. 그들 자신의 것은 모두 남의 것이며, 남의 것은 그들의 것이 아닙니다. 또한 유혹에 빠지기 쉽고 남의 요구에 쉽게 굴복하는 경향이 있으며 말을 아주 잘하고 넘치는 재담에 기지가 있어 사람을 즐겁게 합니다. ',
    '대인관계: 감정기능이 우세해 사람에 대한 관심이 많습니다. 무엇보다 인간관계에서 자발적이며 진실하고자 노력합니다. 이러한 의도는 조용히 타인에게 전해지고, 많은 사람들이 이것에 매력을 느낍니다. 특히 동료들과 잘 어울리고 같이 있기를 좋아하며, 모임을 주도하는 재주가 있습니다. ',
    '대인관계: 매력이 넘치는 대화를 잘하며, 타인의 복잡한 언어구사에도 이해가 빠릅니다. 상대방이 가까운 친지나 친구라고 하더라도 상대에게 불리한 논쟁기술을 곧잘 이용하며 항상 타인보다 유리한 입장을 고수하는 유일한 유형입니다. 또한 남보다 몇 발 앞서며, 수다스럽고 동기부여를 잘하는 이들의 특징은 조직에 생명을 불어넣습니다. ',
    '대인관계 : 자신이 속한 단체에 꾸준히 참여하고 대화합니다. 하지만 다른 사람의 입장과 기분에 잘 대응하지 못하고, 결론에 너무 쉽게 도달하는 경우가 있습니다. 자신과 반대의 의견을 끝까지 경청하려고 하지 않으려 합니다. 따라서 자신들을 전적으로 믿는 사람들의 조언에 귀를 기울여야 하는 노력이 필요합니다.',
    '대인관계: 조화로운 인간관계가 이들에겐 매우 중요합니다. 이들의 기쁨과 만족의 대부분은 주의 사람들의 따뜻한 마음에서 나옵니다. 따라서 다른 사람들이 자신을 좋아하고 존경할 만한 자질에 관심을 기울이는 경향이 있습니다. 또한 동료들의 생활상의 일과 문제점들을 잘 알고 있으며, 상담하는 것을 매우 좋아합니다.',
    '대인 관계 : 사회생활에 유능하며, 이성교제에 능숙합니다. 그리고 어디를 가든 항상 인기가 있습니다. 하지만 다른 사람의 정서까지도 자기의 책임으로 생각하는 경우가 많아 때로 인간관계에 부담이 되기도 합니다. 또한 이상적인 관계를 유지할 수 없는 경우에도 계속 유지하려고 함으로써 상처를 받기 쉽습니다.',    
    '대인 관계 : 자신과 타인의 감정에 관심을 보이고, 자신의 느낌이나 감정을 인정하고 표현하는 것이 필요합니다. 그렇지 않으면 누적된 감정이 크게 폭발할 가능성이 있습니다. 너무 논리와 사고에 의존하기 때문에 감정의 가치를 간과하여 인간관계를 망칠 수 있습니다.',
]

result_text_set3 = [
    '주의할점 : 주어진 일에 몰두하는 경향이 있기 때문에 그 일의 장기적인 의미를 잊기 쉽습니다. 또한 자기 생각이나 방식을 고집하고 지나치게 책임지려는 경향이 있어 상대방을 무시하기 쉽습니다. 따라서 다른 변화나 가능성에도 마음을 열어 놓고 타인의 감정에 민감해질 필요가 있습니다.',
    '주의할점 : 주체성과 독단성이 요구되며, 조용하고 표면에 나서지 않기 때문에 남에게 자기 견해를 발표할 때 확신이 없는 것처럼 보일 수 있어 실제 보다 낮게 평가되기 쉽습니다. 그로 인해 자신의 능력이나 성과를 남에게 알리고 눈에 띄도록 할 필요가 있습니다.그로 인해 자신의 능력이나 성과를 남에게 알리고 눈에 띄도록 할 필요가 있습니다.  ',
    '주의할점: 이상과 현실 사이에서의 괴리 때문에 갈등을 느끼기 쉽습니다. 그로 인해 현실적인 안목을 키워 이상과 현실의 조화시키려는 노력이 필수적입니다. 또한, 외골수로 빠지는 경향이 있기에 조심해야 하며, 너무 지나치게 자신을 의존을 할 수 있기에 주의가 필요합니다.',
    '주의할점 : 조금도 양보가 없어 남들이 그에게 접근하거나 도전하기를 두려워합니다. 타인의 의견에 경청하고 인간적인 면을 살필 줄 알아야 합니다. 남을 인정하는 법을 배우고 비현실적 생각은 버릴 줄 알아야 합니다. 자신의 생각과 행동이 타인에게 미칠 영향도 고려해야 합니다. 다른 사람의 제안을 받아들이는 것을 배울 필요가 있습니다.',
    '주의할점 : 노력을 절약하는 것이 이 성격의 특징입니다. 따라서 열성과 적극성을 키워야 합니다. 일을 미루거나 결말을 짓지 않는 일이 많으므로 인내심을 키워야 합니다. 어떤 일을 결정하기 전에 모든 측면을 숙고하고 고려할 시간여유를 가질 필요가 있습니다. 타인에 대한 고마운 마음을 표현하기 어려워하므로 감정표현을 연습해야 합니다.',
    '주의할점: 무엇보다 자기주장이 너무 없으며, 동조를 잘해 판단력이 부족합니다. 그로 인해 자기 능력과 주장을 내세울 줄 알아야 하며, 상대방에게 부정적인 아픈 말도 해줄 줄 알아야 합니다. 또한 분석적 비판적 사고가 필요하며 보다 미래지향적 인 전망을 일깨울 필요성이 있습니다.',
    '주의할점: 어떤 일에 깊이 관심을 가질 때 완벽주의로 나아가려는 경향이 있습니다. 일을 벌리는 스타일이기에 생각만큼 성취가 되지 않을 때 불안정감을 느끼기도 합니다. 또한 생각하는데 시간을 다 소비하고 행동에 옮기는 것을 어려워해 실질적으로 일하는 법을 배울 필요성이 있습니다.',
    '주의할점: 구체적 사항에 관심을 두고 현실성을 고려해야 합니다. 또한 타인의 개인적인 측면들을 알고자 애쓰고, 타인의 노력을 인정하는 태도를 기를 필요가 있습니다. 뿐만 아니라 지나치게 지적이며 비판적·분석적이어서 인간미가 없다는 말을 듣기 쉽습니다.',

    '주의할점 : 신속하게 행동하고 일ㅆ을 때 남에 대해 둔감하고 무감각하게 보이므로 다른 사람의 감정이나 마음을 보살필 필요가 있습니다. 끈기와 인내, 노력 등 악착스러운 면이 필요합니다. 즉흥적인 행동에만 치우쳐 사전 계획없이 바로 문제에 뛰어드는 경향이 있으므로 마무리 짓는 습관을 길러야 합니다.',
    '주의할점: 논리적, 분석적 사고를 개발할 필요성이 있으며, 일을 시작하기 전에 계획하는 습관을 길러 마무리 할 줄 아는 능력을 길러야 합니다. 또한 일과 레크레이션을 구별할 줄 알아야 하며, 무언가에 뛰어들기 전 심사숙고할 필요가 있습니다. ',
    '주의할점: 한 가지 일을 매듭짓는 법을 배워야 합니다. 현실적인 면도 고려하여 관계된 세부사항을 잘 살피고 좀 꼼꼼해질 필요가 있으며, 일을 벌리지만 말고 우선 순위를 정해놓고 차근차근히 하는 법을 생각해야 합니다. 또한 씀씀이가 커서 항상 미래를 대비할 필요성이 요구됩니다. ',
    '주의할점: 새로운 것을 추구하다 보면 현재의 중요성을 간과하기 쉽습니다. 지나치게 경쟁적이 되지 말고, 다른 사람들의 노력을 인정하며 칭찬할 줄 알아야 합니다. 또한 자기의 능력과 임시 대응기술에 의존하는 경향 때문에 꼭 준비해야 하는 것을 가끔 소홀히 하는 실수를 범하기도 합니다.',
    '주의할점 : 다른 사람의 관점이나 생각을 중시해야 합니다. 현재 외부세계의 정보수집에만 관심을 갖지 않고 새로운 변화의 시도를 고려할 필요가 있습니다. 비논리적이거나 모순된 점을 발견하는 데에만 집중하여, 상대방의 감정에 상처를 줄 수 있습니다.',
    '주의할점: 남을 즐겁게 하는데 신경을 많이 쓰기 때문에 자기 일에 소홀하기 쉽습니다. 또한 일이나 인간관계에 있어 냉철해질 필요가 있으며, 남이 비판적으로 대할 때 마음의 상처를 입기 쉽습니다. 특히 일이나 사람들에 대한 문제에 대하여 냉철한 입장을 취하는 것을 어려워합니다.',
    '주의할점 : 지나치게 다른 사람을 이상화시키지 말고 현실적 안목을 키워야 합니다. 인간관계에 지나치게 끌려서 일을 소홀히 하지 않도록 신경 쓸 필요가 있습니다. 다른 사람의 기분, 인격, 신념 등을 지나치게 동일시하고 공감하는 것을 주의할 필요가 있습니다. 즉, 객관적이 되도록 노력하는 것이 좋습니다.',    
    '주의할점 : 다른 사람의 감정과 말에 귀를 기울이고 인정해줄 필요가 있습니다. 그렇지 않으면 자기자신의 감정을 무시하고 억압하며 다른 사람에게 중압감을 주기 쉽습니다. 또한 따라서 어떤 것을 시작하기 전에 상황의 모든 측면을 고려할 시간이 필요합니다. 그렇지 않으면 속전속결하고 참을성이 없으며 강압적으로 보이기 쉽습니다. ',
]

#Function : HTML Page의 url을 주고 html의 정보를 받아오는 함수
#Input : url
#Return : html
#Data : 2020.07.20
#Author : Jrespect.im
#etc : -
def get_html(url):    
    html = ''    
    res = requests.get(url)    
    if res.status_code == 200:        
        res.encoding = None        
        html = res.text    
    return html


def q1(request):
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page = 1
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])
    return render(request, page_url, {'total1' : total1, 'total2' : total2})

#Function : 질문 Page를 순서대로 처리해주는 함수
#Input : num(page번호)
#Return : q1~q8 : 질문을 선택한 값, total : 이미지url, index_return : 이미지별 index, test : 검사종류결과
#Data : 2020.07.20
#Author : Jrespect.im
#Modify : 현석이형 DB추가 + 결과 텍스트 추가 리턴(200723)
#etc : -
def save_session(request, uname, gender, pswd, mail):
    request.session['uname'] = uname
    request.session['pswd'] = pswd
    request.session['mail'] = mail


def question(request, num):

    if request.method == 'POST':
        uname = request.POST.get('uname')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        email = request.POST.get('email')
        newUser = inputClient(nickname=uname, gender=gender, password=password, email=email)
        newUser.save()

    # HTML에서 선택한(입력된) 내용 받아오기
    if(num > 1): 
        uname = request.GET.get('uname')
        password = request.GET.get('password')
        email = request.GET.get('email')

    q1_1 = request.GET.get('q1-1')
    q1_2 = request.GET.get('q1-2')
    q2_1 = request.GET.get('q2-1')
    q2_2 = request.GET.get('q2-2')
    q3_1 = request.GET.get('q3-1')
    q3_2 = request.GET.get('q3-2')
    q4_1 = request.GET.get('q4-1')
    q4_2 = request.GET.get('q4-2')
    q5_1 = request.GET.get('q5-1')
    q5_2 = request.GET.get('q5-2')
    q6_1 = request.GET.get('q6-1')
    q6_2 = request.GET.get('q6-2')
    q7_1 = request.GET.get('q7-1')
    q7_2 = request.GET.get('q7-2')
    q8_1 = request.GET.get('q8-1')
    q8_2 = request.GET.get('q8-2')


    total1 = [[],[],[],[]] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [[],[],[],[]] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    test = []
    page_url = 'mbti/q%s.html'%num
    myType = []
    Type_hex = 0

    if(num < 9):
        page = num
        for j in range(len(image_name_set)):
            
            if(j < 4):
                total1[0].append(image_name_set[page-1][j])
                total1[1].append(j+1)
            else:
                total2[0].append(image_name_set[page-1][j])
                total2[1].append(j-3)
        #print(total1)
    
    else:
        test += cal(q1_1,q1_2,q2_1,q2_2,q3_1,q3_2,q4_1,q4_2,q5_1,q5_2,q6_1, q6_2, q7_1, q7_2, q8_1, q8_2)
        extra_score = test[1]
        intro_score = test[2]
        sense_score = test[4]
        intui_score = test[5]
        think_score = test[7]
        feel_score = test[8]
        judge_score = test[10]
        percei_score = test[11]

        resultScore = MbtiResult(
        extraScore=extra_score, introScore=intro_score, 
        senseScore=sense_score, intuiScore=intui_score, 
        thinkScore=think_score, feelScore=feel_score, 
        judgeScore=judge_score, perceiScore=percei_score)
        resultScore.save() 
        
        if request.method == 'POST':
            uname = request.POST['uname']
            pswd = request.POST['pswd']
            mail = request.POST['mail']
            resultClient = MbtiResult(nickname=uname, password=pswd, email=mail)
            resultClient.save()
        
        
        extra_score = test[1]
        intro_score = test[2]
        sense_score = test[4]
        intui_score = test[5]
        think_score = test[7]
        feel_score = test[8]
        judge_score = test[10]
        percei_score = test[11]
        
        resultScore = MbtiResult(
        nickname=uname, password=password, email=email,
        extraScore=extra_score, introScore=intro_score, 
        senseScore=sense_score, intuiScore=intui_score, 
        thinkScore=think_score, feelScore=feel_score, 
        judgeScore=judge_score, perceiScore=percei_score)

        resultScore.save()

        for i in range(len(test)):
            if((i % 3) == 0):
                myType += test[i]

        if(myType[0] == 'I'):

            if(myType[1] == 'S'):

                if(myType[2] == 'T'):
                        
                    if(myType[3] == 'J'):
                        Type_hex = 0    
                    else:
                        Type_hex = 1
                else:

                    if(myType[3] == 'J'):
                        Type_hex = 2
                    else:
                        Type_hex = 3
            else:

                if(myType[2] == 'T'):
                        
                    if(myType[3] == 'J'):
                        Type_hex = 4  
                    else:
                        Type_hex = 5  
                else:

                    if(myType[3] == 'J'):
                        Type_hex = 6  
                    else:
                        Type_hex = 7  
                
        else : 
            if(myType[1] == 'S'):

                if(myType[2] == 'T'):
                        
                    if(myType[3] == 'J'):
                        Type_hex = 8  
                    else:
                        Type_hex = 9  
                else:

                    if(myType[3] == 'J'):
                        Type_hex = 10 
                    else:
                        Type_hex = 11
            else:
                if(myType[2] == 'T'):
                        
                    if(myType[3] == 'J'):
                        Type_hex = 12  
                    else:
                        Type_hex = 13 
                else:

                    if(myType[3] == 'J'):
                        Type_hex = 14  
                    else:
                        Type_hex = 15  

        print(test)
        print(myType)
        print(Type_hex)
        print(result_image_set1[Type_hex])
        print(result_text_set[Type_hex])
        print(result_text_set[Type_hex])

    # 위의 값들을 HTML로 넘겨주기
    return render(request, page_url, 
        { 
            'uname' : uname,
            'password' : password ,
            'email' : email,
            'q1_1': q1_1,
            'q1_2': q1_2,
            'q2_1': q2_1,
            'q2_2': q2_2,
            'q3_1': q3_1,
            'q3_2': q3_2,
            'q4_1': q4_1,
            'q4_2': q4_2,
            'q5_1': q5_1,
            'q5_2': q5_2,
            'q6_1': q6_1,
            'q6_2': q6_2,
            'q7_1': q7_1,
            'q7_2': q7_2,
            'q8_1': q8_1,
            'q8_2': q8_2,
            'total1' : total1[0],
            'total2' : total2[0],
            'index_return1' : total1[1],
            'index_return2' : total2[1],
            'test' : test,
            'result_image' : result_image_set1[Type_hex],
            'result_text' : result_text_set[Type_hex],
            'result_text1' : result_text_set1[Type_hex],
            'result_text2' : result_text_set2[Type_hex],
            'result_text3' : result_text_set3[Type_hex]
        } 
    )

#Function : url을 입력하여 포켓몬 이미지를 크롤링 해오는 함수
#Input : request
#Return : total : 이미지url
#Data : 2020.07.20
#Author : Jrespect.im
#etc : 너무오래걸려서 안씁니다
def Crawling_Image(request):
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
     #중복체크용 변수
    key = 0
    #image_name_set의 길이는 8이며-> Index당 8개 데이터로 총 64개 Set
    for j in range(len(image_name_set)):
    #     print(j)
        result = get_html(image_url_set[page][j])   # 이미지를 뽑아올 url_Set Data를 가져옴
        soup = BeautifulSoup(result, 'html.parser') # 뷰티풀 숩을 이용한 HTML 파씽
        tags = soup.select('.wiki-image-wrapper')   # 긁은 사이트가 나무위키이므로 이미지가 저장되어있는 ClassName참조
        
        #Page 1번문제
        if(j < 4):
            for i in tags:
                img =  i.select_one('img')          # 이미지로 되어있는 것을 선택

                if(img) : 
                    image_name = str(img.get('src'))# src의 값을 가져옴

                    # 크롤링해온 이미지의 이름이 긁어올려는 이미지와 갖고 중복이 아닌경우에만
                    if(image_name == (image_name_set[page][j]) and (key == 0)):
                        if((key == 0)):
                            total1.append(image_name_set[page][j])
                            key  = 1

            key = 0 #이미지 1개 크롤링완료 후 중복체크 초기화

        #Page 2번문제
        else:
            for i in tags:
                img =  i.select_one('img')

                if(img) : 
                    image_name = str(img.get('src'))

                    if(image_name == (image_name_set[page][j]) and (key == 0)):
                        if((key == 0)):
                            total2.append(image_name_set[page][j])
                            key  = 1

            key = 0

    #total1 : 질문페이지의 첫번째 질문에 넘겨줄 이미지 name
    #total2 : 질문페이지의 두번째 질문에 넘겨줄 이미지 name
    return render(request, page_url, {'total1' : total1, 'total2' : total2})


# Create your views here.
def intro(request):
    return render(request, 'mbti/intro.html')

def signin(request):
    return render(request, 'mbti/signin.html')

#인증번호 생성함수임
def makeNumber(): 
    _LENGTH = 6 #몇자리?
    stringPool = string.digits # "0123456789"
    certifiNum = "" #결과값
    for n in range(_LENGTH):
        certifiNum += random.choice(stringPool)
    return certifiNum

# 수신자메일 선택함수
def toEmail():
    sendEmail = inputClient.objects.get(email=email)
    
    return 

    #request 로 받아서 넣어주어야 한다.

#메일발송 함수
def sendMail(from_email, to_email, certifiNum):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    smtp.login(from_email, 'zpsdvcrzkzmmkmqr') 
    certifiNum = MIMEText(certifiNum)
    certifiNum['Subject'] = '[인증번호]포켓몬으로 알아보는 성향검사결과 조회'
    certifiNum['To'] = to_email
    smtp.sendmail(from_email, to_email, certifiNum.as_string())
    smtp.quit()

#ajax 보낼수있게 

# def Question(request):
#     return render(request, 'mbti/q1.html')

def info_inquiry(request):     
    return render(request, 'mbti/info_inquiry.html')

#조회화면 후 조회결과 다음 화면 테스트함수
def searchTest(request):
    

    if request.method == 'POST':
        uname = request.POST.get('uname')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        db_Email = MbtiResult.objects.get(email=email)
        extraScore = db_Email.extraScore
        introScore = db_Email.introScore
        senseScore = db_Email.senseScore
        intuiScore = db_Email.intuiScore
        thinkScore = db_Email.thinkScore
        feelScore = db_Email.feelScore
        judgeScore = db_Email.judgeScore
        perceiScore = db_Email.perceiScore

    search_result=0

    if extraScore > 50:
        if senseScore > 50:
            if thinkScore > 50:
                if judgeScore > 50:
                    search_result = 8
                else:
                    search_result = 9
            else:
                if judgeScore > 50:
                    search_result = 10
                else:
                    search_result = 11

        else :
            if thinkScore > 50:
                if judgeScore > 50:
                    search_result = 12
                
                else:
                    search_result = 13

            else:
                if judgeScore > 50:
                    search_result = 14
                
                else:  
                    search_result = 15
    else:
        if senseScore > 50:
            if thinkScore > 50:
                if judgeScore > 50:
                    search_result = 0
                else:
                    search_result = 1
            else:
                if judgeScore > 50:
                    search_result = 2
                else:
                    search_result = 3
        else :
            if thinkScore > 50:
                if judgeScore > 50:
                    search_result = 4
                    
                else:
                    search_result = 5
                        
            else:
                if judgeScore > 50:

                    search_result = 6  
                    
                else:
                    search_result = 7

    print(extraScore, perceiScore)
    return render(request, 'mbti/searchTest.html',
    {
            'extraScore' : extraScore,
            'introScore' : introScore,
            'senseScore' : senseScore,
            'intuiScore' : intuiScore,
            'thinkScore' : thinkScore,
            'feelScore' : feelScore,
            'judgeScore' : judgeScore,
            'perceiScore' : perceiScore,
            'result_image' : result_image_set1[search_result],
            'result_text' : result_text_set[search_result],
            'result_text1' : result_text_set1[search_result],
            'result_text2' : result_text_set2[search_result],
            'result_text3' : result_text_set3[search_result]
    }
    )

# DB보기 함수
def showResult(request):
    mbtiResult = MbtiResult.objects.all()
    return render(request, '/show_result.html', {'list':mbtiResult})

def showQuestion(request):
    question = QuestionList.objects.all()
    return render(request, '/show_question.html',)

def index(request):
    return render(request, 'mbti/index_초기설정.html')

#이메일 중복검사관련 함수
def id_overlap_check(request):
    mail = request.GET.get('mail')
    try: #중복검사실패
        user = User.objects.get(mail = mail)
    except: #중복검사 성공
        user = None #해당 아이디의 user가 없을 경우
    if user is None:
        overlap = '성공 >3<'
    else:
        overlap = '실패 ㅠ!ㅠ'
    context = {'overlap' : overlap}
    return JsonResponse(context)

#Function : 각각의 질문페이지에서 받은 값을 저장하여 MBTI결과를 계산해주는 함수
#Input :  q1~q8 : 질문을 선택한 값
#Return : 타입결과 및 점수
#Data : 2020.07.23
#Author : Jrespect.im / Smalla
#etc : 노가다의 결정체
def cal(q1_1, q1_2, q2_1, q2_2, q3_1, q3_2, q4_1, q4_2, q5_1, q5_2, q6_1, q6_2, q7_1, q7_2, q8_1, q8_2):

    extraIntro = 50       #외향/내향 초기 변수 = 50 
    sensIntu = 50         #감각/직관 초기 변수 = 50
    thinkFeel = 50        #사고/감정 초기 변수 = 50
    judgePerce = 50       #판단/인식 초기 변수 = 50
    
    emotion =[]

    if int(q1_1) == 1:
        extraIntro = extraIntro + 17
    elif int(q1_1) == 2:
        extraIntro = extraIntro + 15
    elif int(q1_1) == 3:
        extraIntro = extraIntro + 11
    elif int(q1_1) == 4:
        extraIntro = extraIntro + 7
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

    #print(myAnswer2)
    if int(q1_2) == 1:
        extraIntro = extraIntro + 18
    elif int(q1_2) == 2:
        extraIntro= extraIntro + 14 
    elif int(q1_2) == 3:
        extraIntro = extraIntro + 12
    elif int(q1_2) == 4:
        extraIntro = extraIntro + 6
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

     #print(myAnswer3)
    if int(q2_1) == 1:
        extraIntro = extraIntro - 5    
    elif int(q2_1) == 2:
        extraIntro= extraIntro - 7   
    elif int(q2_1) == 3:
        extraIntro = extraIntro - 13      
    elif int(q2_1) == 4:
        extraIntro = extraIntro - 15   
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
         
    if int(q2_2) == 1:
        extraIntro = extraIntro -3
    elif int(q2_2) == 2:
        extraIntro = extraIntro - 9
    elif int(q2_2) == 3:
        extraIntro = extraIntro - 11
    elif int(q2_2) == 4:
        extraIntro = extraIntro - 17   
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        
    if int(q3_1) == 1:
        sensIntu = sensIntu +  17
    elif  int(q3_1) == 2:
        sensIntu = sensIntu +  15
    elif  int(q3_1) == 3:
        sensIntu = sensIntu + 11   
    elif  int(q3_1) == 4:
        sensIntu = sensIntu + 7  
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

    if  int(q3_2)== 1:
        sensIntu = sensIntu + 18
    elif  int(q3_2) == 2:
        sensIntu= sensIntu  + 14
    elif  int(q3_2) == 3:
        sensIntu = sensIntu + 12
    elif  int(q3_2) == 4:
        sensIntu = sensIntu + 6   
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        
    if int(q4_1) == 1:
        sensIntu = sensIntu -5
    elif int(q4_1) == 2:
        sensIntu= sensIntu -7
    elif int(q4_1) == 3:
        sensIntu = sensIntu -13     
    elif int(q4_1) == 4:
        sensIntu = sensIntu -15   
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
 
    if int(q4_2) == 1:
        sensIntu = sensIntu -3
    elif int(q4_2)== 2:
        sensIntu= sensIntu  -9   
    elif int(q4_2) == 3:
        sensIntu = sensIntu -11  
    elif int(q4_2) == 4:
        sensIntu = sensIntu -17     
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
    
    if int(q5_1) == 1:
        thinkFeel = thinkFeel + 17     
    elif int(q5_1) == 2:
        thinkFeel= thinkFeel + 15    
    elif int(q5_1) == 3:
        thinkFeel= thinkFeel + 11      
    elif int(q5_1) == 4:
        thinkFeel= thinkFeel + 7   
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
       
    if int(q5_2) == 1:
        thinkFeel = thinkFeel + 18 
    elif int(q5_2) == 2:
        thinkFeel = thinkFeel + 14     
    elif int(q5_2) == 3:
        thinkFeel = thinkFeel + 12     
    elif int(q5_2) == 4:
        thinkFeel= thinkFeel + 6
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
       
    if int(q6_1) == 1:
        thinkFeel = thinkFeel -5
    elif int(q6_1) == 2:
        thinkFeel= thinkFeel -7
    elif int(q6_1)== 3:
        thinkFeel= thinkFeel -13     
    elif int(q6_1) == 4:
        thinkFeel= thinkFeel -15
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
      
    if int(q6_2)== 1:
        thinkFeel = thinkFeel - 3
    elif int(q6_2)== 2:
        thinkFeel = thinkFeel - 9      
    elif int(q6_2) == 3:
        thinkFeel = thinkFeel - 11
    elif int(q6_2) == 4:
        thinkFeel = thinkFeel - 17
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        
 #print(myAnswer2)
    if int(q7_1)== 1:
        judgePerce = judgePerce + 17
    elif int(q7_1)== 2:
        judgePerce= judgePerce + 15   
    elif int(q7_1)== 3:
        judgePerce= judgePerce +11
    elif int(q7_1)== 4:
        judgePerce= judgePerce +7 
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        
    if int(q7_2)== 1:
        judgePerce = judgePerce + 18
    elif  int(q7_2)== 2:
        judgePerce= judgePerce + 14
    elif  int(q7_2)== 3:
        judgePerce= judgePerce + 12
    elif  int(q7_2)== 4:
        judgePerce= judgePerce + 6
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

    if int(q8_1)== 1:
        judgePerce = judgePerce - 5
    elif int(q8_1) == 2:
        judgePerce = judgePerce - 7
    elif int(q8_1) == 3:
        judgePerce = judgePerce - 13
    elif int(q8_1) == 4:
        judgePerce = judgePerce - 15 
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
            
    if int(q8_2)== 1:
        judgePerce = judgePerce -3      
    elif int(q8_2)== 2:
        judgePerce= judgePerce -9          
    elif int(q8_2)== 3:
        judgePerce= judgePerce - 11      
    elif int(q8_2)== 4:
        judgePerce= judgePerce - 17  
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

    rest_extraIntro = 100 - extraIntro
    rest_sensIntu = 100 - sensIntu
    rest_thinkFeel = 100 - thinkFeel
    rest_judgePerce = 100 - judgePerce

    if extraIntro > 50:
        emotion += "E", extraIntro , rest_extraIntro
    else:
        emotion += "I", extraIntro , rest_extraIntro
      
    if  sensIntu > 50:
        emotion += "S", sensIntu , rest_sensIntu
    else:
        emotion += "N", sensIntu , rest_sensIntu

    if thinkFeel > 50:
        emotion += "T", thinkFeel , rest_thinkFeel
    else:
        emotion += "F", thinkFeel , rest_thinkFeel

    if judgePerce > 50:
        emotion += "J", judgePerce , rest_judgePerce
    else:
        emotion += "P", judgePerce , rest_judgePerce

    return emotion
         




