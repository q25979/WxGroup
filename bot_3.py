# -*- coding: UTF-8 -*-
from wxpy import *
from term import *
import time


"""
丙 机器人
"""
class Bot_3:
	def __init__(self):
		self.delay = 30


	# 主函数
	def main(self):
		print "\n============================"
		print u"身份：机器人 丙"
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
		path = "bot3.png"
		self.bot = Bot(
				cache_path=None, console_qr=False, qr_path=path
			)
		print u"登录成功! 系统运行中..."

		# 监听群信息
		@self.bot.register(Group)
		def reply_msg(msg):
			if (msg.text == bot2._1):
				time.sleep(self.delay)
				msg.reply(bot3._1)
			elif (msg.text == bot2._2):
				time.sleep(self.delay)
				msg.reply(bot3._2)
			elif (msg.text == bot4._3):
				time.sleep(self.delay)
				msg.reply(bot3._3)
			elif (msg.text == bot1._6):
				time.sleep(self.delay)
				msg.reply(bot3._4)
			elif (msg.text == bot2._8):
				time.sleep(self.delay)
				msg.reply(bot3._5)
			elif (msg.text == tutor._14):
				time.sleep(self.delay)
				msg.reply(bot3._6)
				time.sleep(self.delay)
				msg.reply(bot3._7)
			elif (msg.text == bot4._4):
				time.sleep(self.delay)
				msg.reply(bot3._8)
			elif (msg.text == bot2._13):
				time.sleep(5)
				msg.reply(bot3._9)
			elif (msg.text == tutor._24):
				time.sleep(self.delay)
				msg.reply(bot3._10)
			elif (msg.text == bot5._3):
				time.sleep(self.delay)
				msg.reply(bot3._11)
			elif (msg.text == bot2._17):
				time.sleep(self.delay)
				msg.reply(bot3._12)
			elif (msg.text == tutor._33):
				time.sleep(self.delay)
				msg.reply(bot3._13)
			elif (msg.text == bot2._19):
				time.sleep(self.delay)
				msg.reply(bot3._14)
			elif (msg.text == bot5._7):
				time.sleep(self.delay)
				msg.reply(bot3._15)
			elif (msg.text == bot2._21):
				time.sleep(self.delay)
				msg.reply(bot3._16)
			elif (msg.text == bot5._8):
				time.sleep(self.delay)
				msg.reply(bot3._17)
			elif (msg.text == bot2._22):
				time.sleep(self.delay)
				msg.reply(bot3._18)
			elif (msg.text == bot4._12):
				time.sleep(self.delay)
				msg.reply(bot3._19)
			elif (msg.text == bot4._13):
				time.sleep(self.delay)
				msg.reply(bot3._20)
			elif (msg.text == bot4._17):
				time.sleep(self.delay)
				msg.reply(bot3._21)
		
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

bot = Bot_3()	# 开启
bot.main()
