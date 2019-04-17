@echo off
color Fd
cls

call:mainFunc 1,2,3,4,5,6,7,8
pause
goto:eof

:mainFunc
	cls
	echo ==================================
	echo = 微信吵群系统         
	echo = 1.全部开启-
	echo = 2.导师开启-
	echo = 3.机器人甲开启-
	echo = 4.机器人乙开启-
	echo = 5.机器人丙开启-
	echo = 6.机器人丁开启-
	echo = 7.机器人戊开启-
	echo = 8.机器人己开启-
	echo ==================================
	set /p val=请输入数字开启对应功能:
	if %1==%val% call:allStart
	if %2==%val% call:tutorStart
	if %3==%val% call:bot1Start
	if %4==%val% call:bot2Start
	if %5==%val% call:bot3Start
	if %6==%val% call:bot4Start
	if %7==%val% call:bot5Start
	if %8==%val% call:bot6Start
	goto:eof

:allStart
	echo 系统启动中...
	start "" cmd /c "title 导师机器人&python tutor.py"
	echo 导师机器人启动成功！
	start "" cmd /c "title 机器人甲&python bot_1.py"
	echo 机器人甲启动成功!
	start "" cmd /c "title 机器人乙&python bot_2.py"
	echo 机器人乙启动成功!
	start "" cmd /c "title 机器人丙&python bot_3.py"
	echo 机器人丙启动成功!
	start "" cmd /c "title 机器人丁&python bot_4.py"
	echo 机器人丁启动成功!
	start "" cmd /c "title 机器人戊&python bot_5.py"
	echo 机器人戊启动成功!
	start "" cmd /c "title 机器人己&python bot_6.py"
	echo 机器人己启动成功!
	set /p go=回复任意继续:
	call:mainFunc 1,2,3,4,5,6,7,8

:tutorStart
	start "" cmd /c "title 导师机器人&python tutor.py"
	echo 导师机器人启动成功!
	set /p go=回复任意继续:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot1Start
	start "" cmd /c "title 机器人甲&python bot_1.py"
	echo 机器人甲启动成功!
	set /p go=回复任意继续:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot2Start
	start "" cmd /c "title 机器人乙&python bot_2.py"
	echo 机器人乙启动成功!
	set /p go=回复任意继续:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot3Start
	start "" cmd /c "title 机器人丙&python bot_3.py"
	echo 机器人丙启动成功!
	set /p go=回复任意继续:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot4Start
	start "" cmd /c "title 机器人丁&python bot_4.py"
	echo 机器人丁启动成功!
	set /p go=回复任意继续:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot5Start
	start "" cmd /c "title 机器人戊&python bot_5.py"
	echo 机器人戊启动成功!
	set /p go=回复任意继续:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot6Start
	start "" cmd /c "title 机器人己&python bot_6.py"
	echo 机器人己启动成功!
	set /p go=回复任意继续:
	call:mainFunc 1,2,3,4,5,6,7,8
