# 텔레그램 뽑기 봇

텔레그램에서 1부터 10까지 랜덤한 숫자를 뽑아주는 봇입니다.

## 사용 방법

1. 텔레그램에서 봇을 생성한 후 봇 토큰을 기록해놓습니다.
2. `main.py`의 'BOT_TOKEN 부분에 1번에 저장한 값을 넣습니다.
3. 웹훅을 통해 해당 서버가 등록된 도메인을 등록합니다, 텔레그램은 https만 지원합니다.(ngrok, heroku, 개인 https 서버 등의 방법 사용)
   - 웹훅 등록 : `curl -X GET https://api.telegram.org/bot{봇 토큰}/getUpdates`
   - 웹훅 삭제 : `curl -X POST https://api.telegram.org/bot{봇 토큰}/setWebhook?remove`
4. 봇이 있는 채팅방에서 `/뽑기` 라고 보내면 랜덤한 숫자를 뽑아줍니다. 

- Procfile, runtime.txt 는 heroku 에서 배포하기 위해 사용한 파일입니다.
