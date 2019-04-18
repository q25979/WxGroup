@echo off
cls

echo 正在安装python环境...
echo 注意全部选择默认
echo 安装成功之后，任意输入进入下一步
start python-2.7.15.amd64.msi
pause

echo 正在添加环境变量...
setx /m PATH "%PATH%;C:\Python27;C:\Python27\Scripts"
echo 环境变量配置成功!

echo 正在安装微信机器人所需环境...
start "" cmd /c "pip install wxpy"

pause