# 0110_metadata

## 목적: Azure Vision API KEY를 .gitignore를 통한 은닉화

### 1. API KEY를 관리해야하는 이유를 알아보았음  
```
API를 만든다는 것은 사용자에게 라이브러리(모듈)을 제공하면서도 OOP의 Encapsulation과 Hiding을 구현하기 위한 방법임
사용자는 API 설계자가 설계한 방식대로 사용할 수 있고
설계자는 KEY를 통하여 API를 사용하는 다수의 사용자의 권한을 개별적으로 조정할 수 있음.
```

### 2. MetaData와 배포 시 .gitignore를 통한 메타데이터 관리를 알아보았음  
- 기존의 코드는 이런 방식으로 누구나 코드에만 접근할 수 있다면 내가 생성한 API KEY에 접근할 수 있었음.
```
headers = { #우리가 보내는 데이터 타입
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': "123456789" #vision-test의 key
}
```
이렇게 만들어져있던 코드를 MetaData로 분리하여 별도의 공간에 저장하고, 모듈을 통해 참조함으로써 사용하였음.
```
headers = { #우리가 보내는 데이터 타입
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.VISION_KEY #vision-test의 key
}
```
- 위와 같은 방식으로 모듈화하여 MetaData로 관리한다면 배포 시 파일의 참조를 끊음으로써 API KEY를 관리할 수 있음
