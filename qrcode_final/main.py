import qrcode


# qr코드 만들어주는 함수
url = 'elderly.ga'   # qr코드 만들려는 url. (배포한 웹사이트 url 기재)
img = qrcode.make(url)
img.save('website.jpg')  # 이미지 저장. (저장될 경로 기입해도 됨)