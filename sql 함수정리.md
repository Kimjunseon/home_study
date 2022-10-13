# group by 사용
```
selcet emp_no, AVG(salary)
   from salaries
```
이 값은 전체 연봉 평균에 사원 1명 값을 가져온다.. 다른 sql 구문에선 오류 발생   
원하는 값은 각 사원 연봉 평균을 구하는 것으로 이때 사용되는 것이 Group by절   
```
selcet emp_no, AVG(salary)
     from salaries
 group by emp_no
```
 
 # sql 함수
 - avg(column) column의 평균
 - sum(column) column의 합
 
 # 날짜 함수
 오늘 날짜 확인
 - select curdate();
 - select current_date;
 
 현재 시간 확인
 - select curtime();
 - select current_time;
 
 현재 시간과 오늘 날짜 동시 확인
 - now()
 - sysdate()
 - select now(), sleep(2), now(); 쿼리가 시작 될때 시작 (슬립에 영향 없음)
 - select sysdate(), sleep(2), sysdate(); 쿼리가 실행 될때 시작 (슬립에 영향 받음)
 
 날짜 포맷
 - select date_format(now(), '%Y년 %m월 %d일 %h:%i:%s');
 - select date_format(now(), '%d %b, \'%y %h:%i:%s'); 미국식 시간 표기
 
 날짜 기간 구하기 (개월 수)
  select emp_no,
	       period_diff(date_format(curdate(), '%y%m'), date_format(hire_date, '%y%m')) as month
	    from employees
	order by month desc;
  
  근속 년수 더하기
  select first_name,
	   hire_date,
       date_add(hire_date, interval 5 year)
  from employees;
  
 abs 절대값
 - select abs(1), abs(-1);

 ceil 천장 수
 -select ceil(3.15), ceiling(3.15);

 mod 나머지
 - select mod(10, 3);

 floor 바닥 수
 - select floor(3.12);
 
 round(x): x에 근접한 정수
 round(x, d): x값 중에 소수점 d자리에 가장 근전합 실수
 - select round(1.498);
 - select round(1.498, 1);
 - select round(1.498, 0);

 power(x, y), pow(x, y): x의 y 제곱 수
 - select pow(2, 3), powwr(2, 3);

 sign(x) 양수는 1, 음수는 -1, 0은 0 출력
 - select sign(-1), sign(1), sign(0);

 greatest(x, y, ...), (x, y, ...) 최대 최소
 - select greatest(10, 40, 20, 50), least(10, 40, 20, 50);
 - select greatest("a", "A", "b", "c", "B", "C"), least("hello", "hela", "hell"); "c"와 "hela" 가 출력
 
 min(colunm), max(colunm) 칼럼에서 최대 최소를 뽑아냄
 
 distinct
  - select distinct(colunm) 칼럼에서 중복제거
  
 substring
  - substring(문자열, index, length)
  - select substring('hello world', 3, 2); ll을 출력함
  
 lpad(오른쪽 정렬), rpad(왼쪽 정렬)
 - select lpad('123', 4, '-'); 출력 -123 숫자 123이 오른쪽에 정렬됨
 - select rpad('123', 4, '-'); 출력 123-
  
 trim, ltrim(왼쪽), rtrim(오른쪽) 공백제거
 - select concat('---', ltrim('   hello   '), '---'); 출력 hello의 좌 공백이 제거되어 출력이 ---hello  ---
 - select	concat('---', rtrim('   hello   '), '---');
 - select	concat('---', trim(both 'x' from'xxxhelxloxxx'), '---');

 
 
 
 
