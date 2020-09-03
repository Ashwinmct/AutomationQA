from selenium.webdriver.support.events import AbstractEventListener


class TestListener(AbstractEventListener):
	def before_navigate_to(self, url, driver):
		print('Before navigating to the url = ', url)

	def after_navigate_to(self, url, driver):
		print('After navigating to the url = ', url)

	def before_navigate_back(self, driver):
		print('Before navigating back to', driver.current_url)

	def after_navigate_back(self, driver):
		print('After navigating back to', driver.current_url)

	def before_navigate_forward(self, driver):
		print('Before navigating forward to', driver.current_url)

	def after_navigate_forward(self, driver):
		print('After navigating forward to', driver.current_url)

	def before_find(self, by, value, driver):
		print('Before find')

	def after_find(self, by, value, driver):
		print('After find')

	def before_click(self, element, driver):
		print('Before clicking')

	def after_click(self, element, driver):
		print('After clicking')

	def before_execute_script(self, script, driver):
		print('Before executing the script')

	def after_execute_script(self, script, driver):
		print('After executing the script')

	def before_quit(self, driver):
		print('Before quiting')

	def after_quit(self, driver):
		print('After quiting')

	def on_exception(self, exception, driver):
		print('On Exception')
