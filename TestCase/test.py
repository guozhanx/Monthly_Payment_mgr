import sys
sys.path.append('../Behavior/')
sys.path.append('../common/')
from Login import Login
from Logout import Logout
import unittest
from selenium import webdriver

class test(unittest.TestCase):
	"""调试登录是否成功"""
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://prep.tingjiandan.com/sso/login?service=http://prep.tingjiandan.com/mgr/login/cas"
		self.verificationErrors = []
		self.accept_next_alert = True
	def test_login(self):
		driver=self.driver
		driver.maximize_window()
		driver.get(self.base_url)
		"""登录"""
		Login().user_login(driver)
		"""退出"""
		Logout().user_logout(driver)
		
if __name__ == '__main__':
	unittest.main()