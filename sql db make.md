# 외부데이터 DB 사용법

## A. workbench 작업
 - Workbench에서 데이터베이스 생성
 - DB 사용자 생성
 - 권한부여
 - 권한 정보 로딩
      - 방법
        1. create database {database_name};   <- 데이터베이스 생성
        2. create user '{user_name}'@'localhost' identified by '{user_password}';   <- DB 사용자 생성 안되면 밑에껄로 수정
            grant all privileges on {user_name}.* to '{user_name}'@'localhost';
        3. grant all privileges on *.* to '{user_name}'@'localhost';   <- 권한부여
        4. flush privileges;   <- 권한 정보 재로딩
      
 ## B. PATH 설정
  - 환경 변수에 mariaDB 중 bin 폴더 내부에 mysql이 들어있는 경로를 추가를 해줌

 ## C. PowerSehll 작업
  - 사용하려는 DB로 cd 구문 사용해 이동
  - 해당 폴더에서 mysql -u {user_name} -p -e "source ./{use.sql}"
  - 리턴 받은 -p 값을 입력
