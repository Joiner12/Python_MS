@echo off
echo Windows focus on

rem 文件夹nothing
echo 文件夹nothing
rd "C:\Users\10520\Desktop\nothing"
md "C:\Users\10520\Desktop\nothing"

pause

rem copy
echo copy
xcopy /s /i /y "C:\Users\10520\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets" "C:\Users\10520\Desktop\nothing"
pause

rem rename
echo rename
ren C:\Users\10520\Desktop\nothing\* *.png
pause

echo cd path
REM cd C:\Users\10520\Desktop\nothing
start "" explorer.exe "C:\Users\10520\Desktop\nothing"
pause

echo del
del C:\Users\10520\Desktop\nothing\*.*
rd C:\Users\10520\Desktop\nothing

