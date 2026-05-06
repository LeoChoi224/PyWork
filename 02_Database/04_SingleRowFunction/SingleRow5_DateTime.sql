-- 날짜 더하기, 빼기
-- DATE_ADD(date, INTERVAL 계산수 계산형식)
-- DATE_SUB(date, INTERVAL 계산수 계산형식)
-- 계산형식이란 월,일,시간 중 어떤걸 더할꺼냐를 선택하는 것이다.  

SELECT
    now()
    , date_add(now(), INTERVAL 1 MONTH) "한달뒤"
    , date_add(now(), INTERVAL 1 DAY) "내일"
    , date_add(now(), INTERVAL 30 DAY) "내일"
;


