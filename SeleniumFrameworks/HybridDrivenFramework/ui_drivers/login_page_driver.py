from utilities.excel import Excel
from .ui_actions import UIActions
from object_repository.property_reader import ReadProperties


class LoginPage:
	global property

	def simulate_login(self, driver, user_name, password):
		excel = Excel()
		properties = ReadProperties()
		login_page = UIActions(driver=driver)
		keywords_file_path = properties.get('KEYWORD_FILE_PATH')
		keywords_sheet_name = properties.get('KEYWORD_SHEET_NAME')
		total_steps = excel.get_number_of_rows(keywords_file_path, keywords_sheet_name)
		for step in range(int(properties.get('STARTING_INDEX')), total_steps):
			keyword_name = excel.read_data_from_sheet(path=keywords_file_path, sheet_name=keywords_sheet_name, row=step,
			                                          column=int(properties.get('KEYWORD_NAME_COLUMN')))
			keyword_type = excel.read_data_from_sheet(path=keywords_file_path, sheet_name=keywords_sheet_name, row=step,
			                                          column=int(properties.get('KEYWORD_TYPE_COLUMN')))
			keyword_value_type = excel.read_data_from_sheet(path=keywords_file_path, sheet_name=keywords_sheet_name,
			                                                row=step,
			                                                column=int(properties.get('KEYWORD_VALUE_COLUMN')))
			keyword_data = excel.read_data_from_sheet(path=keywords_file_path, sheet_name=keywords_sheet_name, row=step,
			                                          column=int(properties.get('KEYWORD_DATA_COLUMN')))
			credential = self.__get_credentials(keyword_name, user_name, password)
			login_page.perform_action(keyword_type, keyword_value_type, keyword_data, credential)
			if keyword_name == 'log_out':
				return self.__analyse_result(driver, properties)
			driver.implicitly_wait(5)

	def __get_credentials(self, name, user_name, password):
		if name == 'user_name':
			return user_name
		if name == 'password':
			return password
		return None

	def __analyse_result(self, driver, properties):
		return 'passed' if driver.title == properties.get('LOGIN_TARGET_PAGE_TITLE') else 'failed'
