@echo off
REM =======================================
REM 특정 포트를 사용하는 프로세스를 종료하는 스크립트
REM 사용법: killport.bat [PORT]
REM 예시:  killport.bat 8080
REM ? 이 파일은 반드시 EUC-KR 로 저장하세요
REM =======================================

if "%~1"=="" (
    echo 사용법: %~nx0 [PORT]
    exit /b 1
)

set PORT=%~1

echo 포트 %PORT% 를 사용하는 프로세스를 찾는 중...

for /f "tokens=5" %%a in ('netstat -ano ^| findstr :%PORT%') do (
    set PID=%%a
)

if not defined PID (
    echo 포트 %PORT% 를 사용하는 프로세스가 없습니다.
    exit /b 0
)

echo 프로세스 ID %PID% 를 강제 종료합니다...
taskkill /F /PID %PID%

echo 완료되었습니다.
