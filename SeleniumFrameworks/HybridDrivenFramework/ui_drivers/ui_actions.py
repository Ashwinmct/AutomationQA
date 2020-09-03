from selenium.webdriver.common.by import By


class UIActions:
	def __init__(self, driver):
		self.driver = driver

	def __get_element(self, element_data_type, element_value):
		element_function_dictionary = {'name': By.NAME,
		                               'xpath': By.XPATH}
		return self.driver.find_element(element_function_dictionary.get(element_data_type), element_value)

	def perform_action(self, object_type, value_type, data, message=None):
		if value_type == 'website_url':
			self.driver.get(data)
			return
		element = self.__get_element(value_type, data)
		if object_type == 'button':
			element.click()
			return
		if object_type == 'text_box':
			element.clear()
			element.send_keys(message)
