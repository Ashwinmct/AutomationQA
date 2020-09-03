import pytest
from selenium import webdriver
from utilities.excel import Excel
from pom_drivers.login_page_driver import LoginPageDriver


class TestLoginPage:
	
	@pytest.fixture()
	def generate_driver(self):
		global driver
		driver = webdriver.Chrome(executable_path=r'C:\Users\VIGNESH\Drivers\chromedriver_win32\chromedriver.exe')
		driver.maximize_window()
		yield driver
		driver.quit()

	@pytest.mark.parametrize('user_name, password, result', [('mercury', 'mercury', 'passed'), ('mercury', 'asd', 'failed')])
	def test_login_page(self, generate_driver, user_name, password, result):
		assert result == self.simulate_login(driver, user_name, password)

	def simulate_login(self, driver, user_name, password):
		excel = Excel()
		login_page = LoginPageDriver(driver=driver)
		keywords_file_path = 'C:\\Users\\VIGNESH\\PycharmProjects\\KDF\\resourses\\keywords.xlsx'
		keywords_sheet_name = 'test'
		total_steps = excel.get_number_of_rows(keywords_file_path, keywords_sheet_name)
		for step in range(1, total_steps):
			keyword_name = excel.read_data_from_sheet(path=keywords_file_path, sheet_name=keywords_sheet_name, row=step,
			                                          column=1)
			keyword_type = excel.read_data_from_sheet(path=keywords_file_path, sheet_name=keywords_sheet_name, row=step,
			                                          column=2)
			keyword_value_type = excel.read_data_from_sheet(path=keywords_file_path, sheet_name=keywords_sheet_name,
			                                           row=step,
			                                           column=3)
			keyword_data = excel.read_data_from_sheet(path=keywords_file_path, sheet_name=keywords_sheet_name, row=step,
			                                          column=4)
			credential = self.__get_credentials(keyword_name, user_name, password)
			login_page.perform_action(keyword_type, keyword_value_type, keyword_data, credential)
			if keyword_name == 'log_out':
				return self.analyse_result(driver)
			driver.implicitly_wait(5)


	def __get_credentials(self, name, user_name, password):
		if name == 'user_name':
			return user_name
		if name == 'password':
			return password
		return None

	def analyse_result(self, driver):
		expected_page_title = 'Login: Mercury Tours'
		return 'passed' if driver.title == expected_page_title else 'failed'
