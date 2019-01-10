import requests
import json
import METADATA

params = {  #또 다른 정보
    'visualFeatures': 'Description',
    'language': 'en'
}

headers = { #우리가 보내는 데이터 타입
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.VISION_KEY #vision-test의 key
}

data = {    #사진 자료
    'url':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Schlagwortkatalog.jpg'
}

res = requests.post('https://koreacentral.api.cognitive.microsoft.com/vision/v1.0/analyze',
                        params=params, headers=headers, json=data)

res_dic = json.loads(res.text)
subscribed_text = res_dic['description']['captions'][0]['text']

#############################################################################################################

params = { 
    'api-version': '3.0',
    'from': 'en',
    'to': 'ko'
}

headers = { #우리가 보내는 데이터의 정보가 담김 타입과 키 
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.TRANSLATE_KEY
}

data = [{ #헤더에서 정의한 데이터 
    'text':subscribed_text 
}]

res = requests.post('https://api.cognitive.microsofttranslator.com/translate', 
                        params=params, headers=headers, json=data)

res_dic = json.loads(res.text)
result = res_dic[0]['translations'][0]['text'] #리스트의 인덱스 분할을 조심할 것 !!!!!!! 리스트의 인덱스 분할은 반드시 정수만 가능 
print(result)
#실제 필요한 데이터는 텍스트기에 디스크립션의 캡션 그리고 리스트의 0번인자의 텍스트를 출력 