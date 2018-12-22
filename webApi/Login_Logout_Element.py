from selenium.webdriver.common.by import By

class Login_Logout_Element(object):
    #定位器，通过元素属性定位元素对象
	def __init__(self):
		"""登录元素"""
		self.username_loc =(By.ID,'username')
		self.password_loc =(By.ID,'password')
		self.submit_loc =(By.ID,'submitForm')

		"""退出元素"""
		self.Loginout=(By.XPATH,".//*[@id='page-wrapper']/div[1]/nav/ul/li[3]/a")
