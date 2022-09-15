##  사용 기술
 * Python 3.4.x
 * Django 1.7.x
 * PostgreSQL
 * 리눅스, 우분투
 * uwsgi
 * celery
 * Windows 서버


## 서버 띄우기

웹 서버

    ./manage.py runserver

http://127.0.0.1:8000/ 접속

celery - 푸시 등의 비동기 작업은 celery 서버를 띄워야 동작한다.

    DJANGO_SETTINGS_MODULE=happytax.settings celery -A accounting.tasks worker -l INFO -E

## 서버 설정
### 서버 배포
1. local 에서 코드 수정 및 확인
2. git 서버에 push
3. aws에 ssh로 접속
4. mtx-ve 로 버철모드 진입
5. mtx-deploy 로 서버 배포 및 서버 재시작

* *주의사항* : /home/ubuntu/happytax/happytax/production.py 에 프로덕션용 세팅이 있음.

<strike>

### 신규 서버
happytax.pem 필요. 혹은 새 서버 등록하는 사람이 key pair 새로 생성하고 바로 auth 실행하면 다른 사람이 작업가능

    fab production auth
    fab -H 호스트명 -- sudo apt-get update

### 새로운 환경 추가 (beta 등)
 * fabfile.py
   * 환경 설정용 task 추가. beta, production 참고
   * server_name, server_alias
   * db_host
 * db backup은 안하도록


### DB 설치 - PostgreSQL
백업을 s3에 하기 때문에 aws credential 필요.

    fab setup_db

pg_hba.conf ip 설정

postgresql.conf listen_addresses 설정

### 웹 설치
 * github 접속용 id_deploy 파일 필요.
 * securevalues.py 필요

다음 명령 실행 - 서버 설정이 바뀔 때마다

    fab production setup_web

소스 변경되었을 때 반영하기

	fab production deploy


### Data Studio를 위한 Proxy설정
    * 설정파일위치 - /etc/haproxy/haproxy.cfg
        * 커넥션 숫자 관리 : global-maxconn, backend-maxconn
        * timeout 관리 : defaults, frontend-timeout

proxy 실행/중지/재시작방법

    ssh-db> sudo service haproxy start/stop/restart
</strike>

## fab 관련 사용 안함

AWS https://mobiletax.signin.aws.amazon.com/console
