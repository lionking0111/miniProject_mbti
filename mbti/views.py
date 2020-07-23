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

#Function : HTML Page의 Value를 받아 URL, PAGE Number를 변환해주는 함수
#Input : Page Number Index
#Return : None
#Data : 2020.07.21
#Author : Jrespect.im
#etc : 개노가다의 흔적...
def page_num(index):
    
    if((index % 8)+1 == 1):
        page = 1
        page_url = 'mbti/q1.html'

    elif((index % 8)+1 == 2):
        page = 2
        page_url = 'mbti/q2.html'

    elif((index % 8)+1 == 3):
        page = 3
        page_url = 'mbti/q3.html'
        
    elif((index % 8)+1 == 4):
        page = 4
        page_url = 'mbti/q4.html'

    elif((index % 8)+1 == 5):
        page = 5
        page_url = 'mbti/q5.html'

    elif((index % 8)+1 == 6):
        page = 6
        page_url = 'mbti/q6.html'

    elif((index % 8)+1 == 7):
        page = 7   
        page_url = 'mbti/q7.html'
    
    elif((index % 8)+1 == 8):
        page = 7   
        page_url = 'mbti/q8.html'

        
    



def q1(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        gender = request.POST['gender']
        pswd = request.POST['pswd']
        mail = request.POST['mail']
        newUser = inputClient(nickname=uname, gender=gender, password=pswd, email=mail)
        resultClient = MbtiResult(nickname=uname, password=pswd, email=mail)
        newUser.save()
        resultClient.save()
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page = 1
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])
    return render(request, page_url, {'total1' : total1, 'total2' : total2})

def q2(request):
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page_url = 'mbti/q2.html'
    page = 2
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])

    return render(request, page_url, {'total1' : total1, 'total2' : total2})

def q3(request):
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page_url = 'mbti/q3.html'
    page = 3
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])

    return render(request, page_url, {'total1' : total1, 'total2' : total2})

def q4(request):
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page_url = 'mbti/q4.html'
    page = 4
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])

    return render(request, page_url, {'total1' : total1, 'total2' : total2})

def q5(request):
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page_url = 'mbti/q5.html'
    page = 5
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])

    return render(request, page_url, {'total1' : total1, 'total2' : total2})

def q6(request):
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page_url = 'mbti/q6.html'
    page = 6
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])

    return render(request, page_url, {'total1' : total1, 'total2' : total2})

def q7(request):
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page_url = 'mbti/q7.html'
    page = 7
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])

    return render(request, page_url, {'total1' : total1, 'total2' : total2})

def q8(request):
    
    total1 = [] #질문페이지 1번문제의 크롤링 이미지를 넘기기 위한 리스트
    total2 = [] #질문페이지 2번문제의 크롤링 이미지를 넘기기 위한 리스트
    page_url = 'mbti/q8.html'
    page = 8
    for j in range(len(image_name_set)):
        if(j < 4):
            total1.append(image_name_set[page-1][j])
        else:
            total2.append(image_name_set[page-1][j])

    return render(request, page_url, {'total1' : total1, 'total2' : total2})


def question(request, num):
    # HTML에서 선택한(입력된) 내용 받아오기
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
    
    print("test:", test)
    # 위의 값들을 HTML로 넘겨주기
    return render(request, page_url, 
        { 
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
            'test' : test
        } 
    )



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
    result = "" #결과값
    for n in range(_LENGTH):
        result += random.choice(stringPool)
    return result
#수신자메일 선택함수
#def toEmail():
 #   sendEmail = inputClient.objects.filter(email)
  #  for e in sendEmail:

#메일발송 함수
def sendMail(from_email, to_email, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    smtp.login(from_email, 'zpsdvcrzkzmmkmqr') 
    msg = MIMEText(msg)
    msg['Subject'] = '[인증번호]포켓몬으로 알아보는 성향검사결과 조회'
    msg['To'] = to_email
    smtp.sendmail(from_email, to_email, makeNumber())
    smtp.quit()
#ajax 보낼수있게 

# def Question(request):
#     return render(request, 'mbti/q1.html')

def q9(request):
    
    return render(request, 'mbti/result.html')

def info_inquiry(request):
    return render(request, 'mbti/info_inquiry.html')

#조회화면 후 조회결과 다음 화면 테스트함수
def searchTest(request):

    return render(request, 'mbti/searchTest.html')


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


def cal(q1_1, q1_2, q2_1, q2_2, q3_1, q3_2, q4_1, q4_2, q5_1, q5_2, q6_1, q6_2, q7_1, q7_2, q8_1, q8_2):

    extraIntro = 50       #외향/내향 초기 변수= 50 
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
        extraIntro = extraIntro + 8
    elif int(q1_2) == 2:
        extraIntro= extraIntro + 10 
    elif int(q1_2) == 3:
        extraIntro = extraIntro + 13
    elif int(q1_2) == 4:
        extraIntro = extraIntro + 19
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

     #print(myAnswer3)
    if int(q2_1) == 1:
        extraIntro = extraIntro - 12    
    elif int(q2_1) == 2:
        extraIntro= extraIntro - 14   
    elif int(q2_1) == 3:
        extraIntro = extraIntro - 6      
    elif int(q2_1) == 4:
        extraIntro = extraIntro - 18   
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
         
    if int(q2_2) == 1:
        extraIntro = extraIntro -5
    elif int(q2_2) == 2:
        extraIntro = extraIntro - 9
    elif int(q2_2) == 3:
        extraIntro = extraIntro - 16
    elif int(q2_2) == 4:
        extraIntro = extraIntro - 20   
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
        sensIntu = sensIntu + 19
    elif  int(q3_2) == 2:
        sensIntu= sensIntu  + 13
    elif  int(q3_2) == 3:
        sensIntu = sensIntu + 10
    elif  int(q3_2) == 4:
        sensIntu = sensIntu + 8    
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
        
    if int(q4_1) == 1:
        sensIntu = sensIntu -6
    elif int(q4_1) == 2:
        sensIntu= sensIntu -12
    elif int(q4_1) == 3:
        sensIntu = sensIntu -14     
    elif int(q4_1) == 4:
        sensIntu = sensIntu -18   
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
 
    if int(q4_2) == 1:
        sensIntu = sensIntu -5
    elif int(q4_2)== 2:
        sensIntu= sensIntu  -9   
    elif int(q4_2) == 3:
        sensIntu = sensIntu -16  
    elif int(q4_2) == 4:
        sensIntu = sensIntu -20     
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
        thinkFeel = thinkFeel + 19   
    elif int(q5_2) == 2:
        thinkFeel = thinkFeel + 13     
    elif int(q5_2) == 3:
        thinkFeel = thinkFeel + 10     
    elif int(q5_2) == 4:
        thinkFeel= thinkFeel + 8
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
       
    if int(q6_1) == 1:
        thinkFeel = thinkFeel -6   
    elif int(q6_1) == 2:
        thinkFeel= thinkFeel -12
    elif int(q6_1)== 3:
        thinkFeel= thinkFeel -14     
    elif int(q6_1) == 4:
        thinkFeel= thinkFeel -18
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
      
    if int(q6_2)== 1:
        thinkFeel = thinkFeel - 20
    elif int(q6_2)== 2:
        thinkFeel = thinkFeel - 16      
    elif int(q6_2) == 3:
        thinkFeel = thinkFeel - 9
    elif int(q6_2) == 4:
        thinkFeel = thinkFeel - 5
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
        judgePerce = judgePerce + 19
    elif  int(q7_2)== 2:
        judgePerce= judgePerce + 13
    elif  int(q7_2)== 3:
        judgePerce= judgePerce + 10
    elif  int(q7_2)== 4:
        judgePerce= judgePerce + 8
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")

    if int(q8_1)== 1:
        judgePerce = judgePerce - 6
    elif int(q8_1) == 2:
        judgePerce = judgePerce - 12
    elif int(q8_1) == 3:
        judgePerce = judgePerce - 14
    elif int(q8_1) == 4:
        judgePerce = judgePerce - 18 
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
            
    if int(q8_2)== 1:
        judgePerce = judgePerce -5        
    elif int(q8_2)== 2:
        judgePerce= judgePerce -9          
    elif int(q8_2)== 3:
        judgePerce= judgePerce - 16      
    elif int(q8_2)== 4:
        judgePerce= judgePerce - 20  
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
         





