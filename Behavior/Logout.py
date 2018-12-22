#公共模块，登录和退出
import sys
sys.path.append('../webApi')
sys.path.append('../common')
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
import datetime
from logger import Log
from selenium.webdriver.common.by import By
from Login_Logout_Element import Login_Logout_Element
nowTime=datetime.datetime.now().strftime('%Y-%m-%d:%H:%M:%S')


class Logout(unittest.TestCase,Login_Logout_Element):
	"""初始化element"""
	def __init__(self):
		Login_Logout_Element.__init__(self)
	def user_logout(self,driver):
		"""退出登录"""
		try:
			Loginout = driver.find_element(*self.Loginout).click()
			Log().info("退出登录成功！")
			"""关闭浏览器"""
			sleep(5)
			driver.quit()
		except Exception as e:
			print(e)


		
