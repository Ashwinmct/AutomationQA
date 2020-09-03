class Site(object):
	def __init__(self, driver):
		self.driver = driver


class LogInPage(Site):
	login_page_url = 'http://demo.guru99.com/test/newtours/index.php'

	def __init__(self, driver):
		super().__init__(driver)


	def enter_user_name(self, message):
		user_field = 'userName'
		self.__send_message(user_field, message)

	def enter_password(self, message):
		self.__send_message('password', message)

	def click_log_in(self):
		(self.__get_element('submit')).click()

	def __get_element(self, name):
		return self.driver.find_element_by_name(name)

	def restart(self):
		self.driver.get(self.login_page_url)

	def __send_message(self, element_name, message):
		element = self.__get_element(element_name)
		element.clear()
		element.send_keys(message)