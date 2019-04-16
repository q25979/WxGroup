# -*- coding: UTF-8 -*-
from wxpy import *


"""
转换为中文发送
str 需要发送的信息
"""
def change_to_chinese(str):
	return str.decode("utf8")


"""
获取好友微信好友所有列表
obj 初始化机器人对象
"""
def get_all_friends(obj):
	return obj.friends()


# 初始化机器人
bot = Bot()
# bot.file_helper.send(change_to_chinese("你好")) # 发助手
# print bot.friends() # 获取所有好友
# print bot.groups()  # 获取所有群
