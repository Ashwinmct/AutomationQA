import pytest
from selenium import webdriver
from ui_drivers.login_page_driver import LoginPage
from utilities.excel import Excel
from ui_drivers.constants import Constants
from object_repository.property_reader import ReadProperties


class TestLogin:
	@pytest.fixture()
	def generate_driver(self):
		global driver
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		options.add_argument('--no-sandbox')
		driver = webdriver.Chrome(executable_path=Constants.CHROME_PATH.value,options=options)
		driver.maximize_window()
		yield driver
		driver.quit()

	def test_login_page(self, generate_driver):
		excel = Excel()
		login = LoginPage()
		properties = ReadProperties()
		total_users = excel.get_number_of_rows(properties.get('DATA_FILE_PATH'), properties.get('DATA_SHEET_NAME'))
		for user in range(int(properties.get('STARTING_INDEX')), total_users):
			user_name = excel.read_data_from_sheet(properties.get('DATA_FILE_PATH'), properties.get('DATA_SHEET_NAME'), user, int(properties.get('DATA_NAME_COLUMN')))
			pass_word = excel.read_data_from_sheet(properties.get('DATA_FILE_PATH'), properties.get('DATA_SHEET_NAME'), user, int(properties.get('DATA_PASSWORD_COLUMN')))
			result = excel.read_data_from_sheet(properties.get('DATA_FILE_PATH'), properties.get('DATA_SHEET_NAME'), user, int(properties.get('DATA_RESULT_COLUMN')))
			login_result = login.simulate_login(driver, user_name, pass_word)
			assert result == login_result
