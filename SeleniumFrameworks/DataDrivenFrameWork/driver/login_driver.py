import time
from pom_classes.login_page import LogInPage


class LoginDriver():
	@classmethod
	def simulate_login(cls, driver, user_name, pass_word, result):
		login = LogInPage(driver)
		login.restart()
		login.enter_user_name(user_name)
		login.enter_password(pass_word)
		login.click_log_in()
		time.sleep(5)
		return cls.check_result(driver, result)

	@classmethod
	def check_result(cls, driver, expected_result):
		target_page_url = 'http://demo.guru99.com/test/newtours/login_sucess.php'
		result = 'passed' if driver.current_url == target_page_url else 'failed'
		return result == expected_result
