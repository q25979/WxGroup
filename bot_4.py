# -*- coding: UTF-8 -*-
from wxpy import *
from term import *
import time


"""
丁 机器人
"""
class Bot_4:
	def __init__(self):
		self.delay = 20
		self.imgwin = "./img/_4zj.jpg"
		self.imgprofit = "./img/_4yl2.jpg"
		self.imgprofit2 = "./img/_4yl3.jpg"


	# 主函数
	def main(self):
		print "\n============================"
		print u"身份：机器人 丁"
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
		path = "bot4.png"
		self.bot = Bot(
				cache_path=None, console_qr=False, qr_path=path
			)
		print u"登录成功! 系统运行中..."

		# 监听群信息
		@self.bot.register(Group)
		def reply_msg(msg):
			if (msg.text == bot3._1):
				time.sleep(self.delay)
				msg.reply(bot4._1)
			elif (msg.text == bot3._2):
				time.sleep(self.delay)
				msg.reply(bot4._2)
			elif (msg.text == bot2._7):
				time.sleep(self.delay)
				msg.reply(bot4._3)
			elif (msg.text == bot3._7):
				time.sleep(self.delay)
				msg.reply(bot4._4)
			elif (msg.text == bot3._8):
				time.sleep(self.delay)
				msg.reply(bot4._5)
			elif (msg.text == tutor._16):
				time.sleep(self.delay)
				msg.reply(bot4._6)
			elif (msg.text == tutor._17):
				time.sleep(5)
				msg.reply(bot4._7)
			elif (msg.text == tutor._22):
				time.sleep(self.delay)
				msg.reply(bot4._8)
			elif (msg.text == bot2._12):
				time.sleep(5)
				msg.reply(bot4._9)
			elif (msg.text == tutor._28):
				time.sleep(self.delay)
				msg.reply(bot4._10)
				time.sleep(3)
				msg.reply_image(self.imgprofit)	#  盈利截图2
			elif (msg.text == bot1._14):
				time.sleep(self.delay)
				msg.reply(bot4._11)
			elif (msg.text == bot2._24):
				time.sleep(self.delay)
				msg.reply(bot4._12)
				time.sleep(3)
				msg.reply_image(self.imgprofit2)	#  盈利截图3
			elif (msg.text == bot2._25):
				time.sleep(self.delay)
				msg.reply(bot4._13)
			elif (msg.text == bot2._26):
				time.sleep(self.delay)
				msg.reply(bot4._14)
			elif (msg.text == bot2._27):
				time.sleep(self.delay)
				msg.reply(bot4._15)
			elif (msg.text == bot5._10):
				time.sleep(self.delay)
				msg.reply(bot4._16)
			elif (msg.text == bot5._11):
				time.sleep(self.delay)
				msg.reply(bot4._17)
			elif (msg.text == bot3._21):
				time.sleep(self.delay)
				msg.reply(bot4._18)
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

bot = Bot_4()	# 开启
bot.main()
