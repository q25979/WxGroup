# -*- coding: UTF-8 -*-
from wxpy import *
from term import *
import time


"""
导师机器人
"""
class Tutor:
	def __init__(self):
		self.delay = 2	# 2秒延时


	# 主函数
	def main(self):
		print "\n============================"
		print u"身份：导师"
		print u"回复数字实现对应功能："
		print u"1.登录"
		print u"2.获取所有群"
		print u"3.开始启动"
		print u"4.停止系统"
		print u"5.退出系统"
		print "============================"
		itext = "请输入数字："
		ifunc = input(itext.decode("UTF-8").encode("GBK"))
		
		if ifunc == 1:
			self.login()
		elif ifunc == 2:
			self.get_all_group()
		elif ifunc == 3:
			self.start()
		elif ifunc == 4:
			self.stop()
		elif ifunc == 5:
			self.exit()
		else:
			print u"输入错误请重新输入"
			self.main()


	# 登录微信
	def login(self):
		print u"正在下载二维码，请等待..."
		path = "tutor.png"
		self.bot = Bot(
				cache_path=None, console_qr=False, qr_path=path
			)
		print u"登录成功!"

		# 监听群信息
		@self.bot.register(Group)
		def reply_msg(msg):
			if (msg.text == bot4._1):
				time.sleep(2)
				msg.reply(tutor._2)
			elif (msg.text == bot4._2):
				time.sleep(5)
				msg.reply(tutor._3)
			elif (msg.text == bot2._4):
				time.sleep(2)
				msg.reply(tutor._4)
			elif (msg.text == bot1._2):
				time.sleep(3)
				msg.reply(tutor._5)
			elif (msg.text == bot1._3):
				time.sleep(10)
				msg.reply(tutor._6)
			elif (msg.text == bot2._5):
				time.sleep(2)
				msg.reply(tutor._7)
				time.sleep(4)
				msg.reply(tutor._8)
			elif (msg.text == bot2._6):
				time.sleep(3)
				msg.reply(tutor._9)
			elif (msg.text == bot1._5):
				time.sleep(3)
				msg.reply(tutor._10)
				time.sleep(5)
				msg.reply(tutor._11)
			elif (msg.text == bot3._3):
				time.sleep(5)
				msg.reply(tutor._12)
			elif (msg.text == bot3._4):
				time.sleep(8)
				msg.reply(tutor._13)
			elif (msg.text == bot3._5):
				time.sleep(5)
				msg.reply(tutor._14)
			elif (msg.text == bot4._5):
				time.sleep(5)
				msg.reply(tutor._15)
			elif (msg.text == bot2._9):
				time.sleep(10)
				msg.reply(tutor._16)
			elif (msg.text == bot4._6):
				time.sleep(2)
				msg.reply(tutor._17)
			elif (msg.text == bot4._7):
				time.sleep(2)
				msg.reply(tutor._18)
			elif (msg.text == bot1._8):
				time.sleep(2)
				msg.reply(tutor._19)
			elif (msg.text == bot2._10):
				time.sleep(6)
				msg.reply(tutor._20)
			elif (msg.text == bot2._11):
				time.sleep(1)
				msg.reply(tutor._21)
				time.sleep(1.5)
				msg.reply(tutor._22)
			elif (msg.text == bot1._9):
				time.sleep(3)
				msg.reply(tutor._23)
				time.sleep(1)
				msg.reply(tutor._24)
			elif (msg.text == bot3._10):
				time.sleep(3)
				msg.reply(tutor._25)
			elif (msg.text == bot1._10):
				time.sleep(1.5)
				msg.reply(tutor._26)
				time.sleep(2)
				msg.reply(tutor._27)
			elif (msg.text == bot1._11):
				time.sleep(1)
				msg.reply(tutor._28)
			elif (msg.text == bot4._10):
				time.sleep(2)
				msg.reply(tutor._29)
			elif (msg.text == bot2._15):
				time.sleep(2)
				msg.reply(tutor._30)
				time.sleep(6)
				msg.reply(tutor._31)
			elif (msg.text == bot2._16):
				time.sleep(2)
				msg.reply(tutor._32)
			elif (msg.text == bot5._5):
				time.sleep(8)
				msg.reply(tutor._33)
			elif (msg.text == bot3._13):
				time.sleep(8)
				msg.reply(tutor._34)
			elif (msg.text == bot4._15):
				time.sleep(3)
				msg.reply(tutor._35)
		
		self.main()


	# 获取二维码后回调
	def qr_func(self, uuid, status, qrcode):
		"""
		使用生成不了二维码，得自己生成二维码
		"""
		print "uuid: %s,  status: %s" % (uuid, status)
		print u"二维码获取成功!"


	# 登录成功
	def login_func(self):
		print u"登录成功!"


	# 注销成功
	def logout_func(self):
		print u"注销成功!"


	# 获取所有群
	def get_all_group(self):
		all_group = self.bot.groups()
		print all_group

		str_group = ""
		for li in all_group:
			str_group = str_group + str(li)[8:-1] + "\n"

		# 保存所有群到文件中
		file = open("./groups.list", 'w+')
		file.write(str_group)
		file.close()
		print u"获取成功，所有群保存在groups.list文件中，请到该文件删除不需要的群。"
		self.main()


	# 开始启动
	def start(self):
		print u"开始启动,读取群信息..."
		file = open("./groups.list", 'r+')
		lists = file.read()
		file.close()
		groups = filter(None, lists.split("\n"))	# 群名称
		for li in groups:
			# 搜索聊天对象
			mygroup = self.bot.groups().search(li)
			mygroup[0].send(tutor._1)
			print li + u"发送成功！"
			time.sleep(0.5)
		self.main()


	# 停止系统
	def stop(self):
		self.bot.logout()
		print u"账号注销成功"
		self.main()


	# 退出系统
	def exit(self):
		self.bot.logout()
		print u"退出系统成功"


tutor = TermTutor()
bot1  = Bot1()	# 甲
bot2  = Bot2()
bot3  = Bot3()
bot4  = Bot4()
bot5  = Bot5()
bot6  = Bot6()

bot = Tutor()	# 开启
bot.main()
