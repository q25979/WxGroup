# -*- coding: UTF-8 -*-
from wxpy import *
import time


"""
导师机器人
"""
class Tutor:
	def __init__(self):
		pass


	# 主函数
	def main(self):
		print "\n============================"
		print u"回复数字实现对应功能："
		print u"1.获取所有群"
		print u"2.开始启动"
		print u"3.停止系统"
		print u"4.退出系统"
		print u"5.登录"
		print "============================"
		itext = "请输入数字："
		ifunc = input(itext.decode("UTF-8").encode("GBK"))
		
		if ifunc == 1:
			self.get_all_group()
		elif ifunc == 2:
			self.start()
		elif ifunc == 3:
			self.stop()
		elif ifunc == 4:
			self.exit()
		elif ifunc == 5:
			self.login()
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
			mygroup[0].send('Hello')
			print mygroup[0] + u"发送成功！"
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


# 开启
bot = Tutor()
bot.main()
