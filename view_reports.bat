@echo off
echo ========================================
echo Opening Locust Test Reports
echo ========================================
echo.

REM Check if HTML report exists
if exist "reports\html_reports\report.html" (
    echo [OK] Opening HTML report in browser...
    start "" "reports\html_reports\report.html"
    echo.
) else (
    echo [!] HTML report not found at: reports\html_reports\report.html
    echo [!] Please run the load test first using: run_tests.bat
    echo.
)

REM Check if CSV reports exist
if exist "reports\json_reports\locust_report_stats.csv" (
    echo [OK] CSV reports found in: reports\json_reports\
    echo.
    choice /C YN /M "Do you want to open the CSV stats file"
    if errorlevel 2 goto :skip_csv
    if errorlevel 1 goto :open_csv
    
    :open_csv
    start "" "reports\json_reports\locust_report_stats.csv"
    echo [OK] Opening CSV stats file...
    echo.
    
    :skip_csv
) else (
    echo [!] CSV reports not found
    echo [!] Please run the load test first using: run_tests.bat
    echo.
)

echo ========================================
echo Report Locations:
echo ========================================
echo HTML: reports\html_reports\report.html
echo CSV:  reports\json_reports\
echo ========================================
echo.

pause
