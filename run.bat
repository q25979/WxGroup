@echo off
color Fd
cls

call:mainFunc 1,2,3,4,5,6,7,8
pause
goto:eof

:mainFunc
	cls
	echo ==================================
	echo = ΢�ų�Ⱥϵͳ         
	echo = 1.ȫ������-
	echo = 2.��ʦ����-
	echo = 3.�����˼׿���-
	echo = 4.�������ҿ���-
	echo = 5.�����˱�����-
	echo = 6.�����˶�����-
	echo = 7.�������쿪��-
	echo = 8.�����˼�����-
	echo ==================================
	set /p val=���������ֿ�����Ӧ����:
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
	echo ϵͳ������...
	start "" cmd /c "title ��ʦ������&python tutor.py"
	echo ��ʦ�����������ɹ���
	start "" cmd /c "title �����˼�&python bot_1.py"
	echo �����˼������ɹ�!
	start "" cmd /c "title ��������&python bot_2.py"
	echo �������������ɹ�!
	start "" cmd /c "title �����˱�&python bot_3.py"
	echo �����˱������ɹ�!
	start "" cmd /c "title �����˶�&python bot_4.py"
	echo �����˶������ɹ�!
	start "" cmd /c "title ��������&python bot_5.py"
	echo �������������ɹ�!
	start "" cmd /c "title �����˼�&python bot_6.py"
	echo �����˼������ɹ�!
	set /p go=�ظ��������:
	call:mainFunc 1,2,3,4,5,6,7,8

:tutorStart
	start "" cmd /c "title ��ʦ������&python tutor.py"
	echo ��ʦ�����������ɹ�!
	set /p go=�ظ��������:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot1Start
	start "" cmd /c "title �����˼�&python bot_1.py"
	echo �����˼������ɹ�!
	set /p go=�ظ��������:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot2Start
	start "" cmd /c "title ��������&python bot_2.py"
	echo �������������ɹ�!
	set /p go=�ظ��������:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot3Start
	start "" cmd /c "title �����˱�&python bot_3.py"
	echo �����˱������ɹ�!
	set /p go=�ظ��������:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot4Start
	start "" cmd /c "title �����˶�&python bot_4.py"
	echo �����˶������ɹ�!
	set /p go=�ظ��������:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot5Start
	start "" cmd /c "title ��������&python bot_5.py"
	echo �������������ɹ�!
	set /p go=�ظ��������:
	call:mainFunc 1,2,3,4,5,6,7,8

:bot6Start
	start "" cmd /c "title �����˼�&python bot_6.py"
	echo �����˼������ɹ�!
	set /p go=�ظ��������:
	call:mainFunc 1,2,3,4,5,6,7,8
