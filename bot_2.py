# -*- coding: UTF-8 -*-
from wxpy import *
from term import *
import time


"""
乙 机器人
"""
class Bot_2:
	def __init__(self):
		self.delay = 16
		self.imgpath = "./img/qrcode.jpg"
		self.imgtz = "./img/_2tz.jpg"
		self.imgyl = "./img/_2yl.jpg"
		self.imgyl2 = "./img/_2yl2.jpg"


	# 主函数
	def main(self):
		print "\n============================"
		print u"身份：机器人 乙"
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
		path = "bot2.png"
		self.bot = Bot(
				cache_path=None, console_qr=False, qr_path=path
			)
		print u"登录成功! 系统运行中..."

		# 监听群信息
		@self.bot.register(Group)
		def reply_msg(msg):
			if (msg.text == bot1._1):
				time.sleep(self.delay)
				msg.reply(bot2._1)
			elif (msg.text == tutor._2):
				time.sleep(self.delay)
				msg.reply(bot2._2)
			elif (msg.text == tutor._3):
				time.sleep(self.delay)
				msg.reply(bot2._3)
				time.sleep(self.delay)
				msg.reply(bot2._4)
			elif (msg.text == bot1._4):
				time.sleep(self.delay)
				msg.reply(bot2._5)
			elif (msg.text == tutor._8):
				time.sleep(self.delay)
				msg.reply(bot2._6)
			elif (msg.text == tutor._11):
				time.sleep(self.delay)
				msg.reply(bot2._7)
			elif (msg.text == bot1._7):
				time.sleep(self.delay)
				msg.reply(bot2._8)
			elif (msg.text == tutor._15):
				time.sleep(self.delay)
				msg.reply(bot2._9)
			elif (msg.text == tutor._19):
				time.sleep(self.delay)
				msg.reply(bot2._10)
			elif (msg.text == tutor._20):
				time.sleep(self.delay)
				msg.reply(bot2._11)
			elif (msg.text == bot4._8):
				time.sleep(self.delay)
				msg.reply(bot2._12)
			elif (msg.text == bot4._9):
				time.sleep(self.delay)
				msg.reply(bot2._13)
			elif (msg.text == bot3._9):
				time.sleep(self.delay)
				msg.reply(bot2._14)
			elif (msg.text == bot5._1):
				time.sleep(3)
				msg.reply_image(self.imgpath)	#  导师二维码
				time.sleep(3)
				msg.reply(bot2._15)
			elif (msg.text == bot5._2):
				time.sleep(self.delay)
				msg.reply(bot2._16)
			elif (msg.text == bot5._4):
				time.sleep(self.delay)
				msg.reply(bot2._17)
			elif (msg.text == tutor._34):
				time.sleep(self.delay)
				msg.reply(bot2._18)
			elif (msg.text == bot1._12):
				time.sleep(self.delay)
				msg.reply(bot2._19)
			elif (msg.text == bot3._14):
				time.sleep(self.delay)
				msg.reply(bot2._20)
			elif (msg.text == bot3._15):
				time.sleep(self.delay)
				msg.reply(bot2._21)
			elif (msg.text == bot3._17):
				time.sleep(self.delay)
				msg.reply(bot2._22)
			elif (msg.text == bot1._13):
				time.sleep(self.delay)
				msg.reply(bot2._23)
			elif (msg.text == bot6._2):
				time.sleep(self.delay)
				msg.reply_image(self.imgtz)	#  投注截图
				time.sleep(3)
				msg.reply(bot2._24)
			elif (msg.text == bot3._19):
				time.sleep(self.delay)
				msg.reply_image(self.imgyl)	#  盈利截图
				time.sleep(3)
				msg.reply(bot2._25)
			elif (msg.text == bot3._20):
				time.sleep(self.delay)
				msg.reply(bot2._26)
			elif (msg.text == bot4._14):
				time.sleep(self.delay)
				msg.reply(bot2._27)
			elif (msg.text == bot4._18):
				time.sleep(self.delay)
				msg.reply(bot2._28)
				time.sleep(3)
				msg.reply_image(self.imgyl2)	#  盈利截图

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

bot = Bot_2()	# 开启
bot.main()
