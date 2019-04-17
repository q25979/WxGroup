# -*- coding: UTF-8 -*-
from wxpy import *
from term import *
import time


"""
己 机器人
"""
class Bot_6:
	def __init__(self):
		self.delay = 3


	# 主函数
	def main(self):
		print "\n============================"
		print u"身份：机器人 己"
		print u"回复数字实现对应功能："
		print u"1.登录"
		print u"2.停止系统"
		print "============================"
		itext = "请输入数字："
		ifunc = input(itext.decode("UTF-8").encode("GBK"))
		
		if ifunc == 1:
			self.login()
		elif ifunc == 2:
			self.stop()
		else:
			print u"输入错误请重新输入"
			self.main()


	# 登录微信
	def login(self):
		print u"正在下载二维码，请等待..."
		path = "bot6.png"
		self.bot = Bot(
				cache_path=None, console_qr=False, qr_path=path
			)
		print u"登录成功! 系统运行中..."

		# 监听群信息
		@self.bot.register(Group)
		def reply_msg(msg):
			if (msg.text == bot4._11):
				time.sleep(self.delay)
				msg.reply(bot6._1)
				time.sleep(self.delay)
				msg.reply(bot6._2)
		
		self.main()


	# 登录成功
	def login_func(self):
		print u"登录成功!"


	# 注销成功
	def logout_func(self):
		print u"注销成功!"


	# 停止系统
	def stop(self):
		self.bot.logout()
		print u"账号注销成功"
		self.main()


tutor = TermTutor()
bot1  = Bot1()	# 甲
bot2  = Bot2()
bot3  = Bot3()
bot4  = Bot4()
bot5  = Bot5()
bot6  = Bot6()

bot = Bot_6()	# 开启
bot.main()
