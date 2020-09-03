import pytest
import time
from selenium import webdriver
from utilities.excel import Excel
from pom_classes.login_page import LogInPage
from utilities.json import JSONreader
from driver.login_driver import LoginDriver


class TestLogInPage:
	excel = Excel()
	user_details_file_path = "C:\\Users\\VIGNESH\\PycharmProjects\\DDF\\resource\\UserDetails.xlsx"

	@pytest.fixture()
	def get_driver_object(self):
		global driver
		driver = webdriver.Chrome(executable_path=r'C:\Users\VIGNESH\Drivers\chromedriver_win32\chromedriver.exe')
		driver.maximize_window()
		yield driver
		driver.quit()

	def test_login_page_with_xl(self, get_driver_object):
		sheet_name = "login"
		total_users_data = self.excel.get_number_of_rows(self.user_details_file_path, sheet_name)
		for row in range(1, total_users_data):
			user_name = self.excel.read_data_from_sheet(self.user_details_file_path, sheet_name, row, 0)
			pass_word = self.excel.read_data_from_sheet(self.user_details_file_path, sheet_name, row, 1)
			expected_result = self.excel.read_data_from_sheet(self.user_details_file_path, sheet_name, row, 2)
			assert LoginDriver.simulate_login(driver, user_name, pass_word, expected_result)

	def test_login_page_with_json(self, get_driver_object):
		path = "C:\\Users\\VIGNESH\\PycharmProjects\\DDF\\resource\\UserDetails.json"
		user_details = JSONreader.load_file(path)
		for user in user_details['credentials']:
			user_name = user['username']
			pass_word = user['password']
			result = user['result']
			assert LoginDriver.simulate_login(driver, user_name, pass_word, result)
