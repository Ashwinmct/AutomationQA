class LoginPageDriver:
	def __init__(self, driver):
		self.driver = driver

	def __get_element(self, element_data_type, element_value):
		if element_data_type == 'name':
			return self.driver.find_element_by_name(element_value)
		return self.driver.find_element_by_xpath(element_value)

	def perform_action(self, object_type, value_type, data, message=None):
		if value_type == 'website_url':
			self.driver.get(data)
			return
		element = self.__get_element(object_type, data)
		if value_type == 'button':
			element.click()
			return
		if value_type == 'text_box':
			element.clear()
			element.send_keys(message)
