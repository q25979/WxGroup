@echo off
cls

echo ���ڰ�װpython����...
echo ע��ȫ��ѡ��Ĭ��
echo ��װ�ɹ�֮���������������һ��
start python-2.7.15.amd64.msi
pause

echo ������ӻ�������...
setx /m PATH "%PATH%;C:\Python27;C:\Python27\Scripts"
echo �����������óɹ�!

echo ���ڰ�װ΢�Ż��������軷��...
start "" cmd /c "pip install wxpy"

pause