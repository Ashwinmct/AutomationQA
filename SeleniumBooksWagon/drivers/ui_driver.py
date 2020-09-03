from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class UIDriver(object):
	DEFAULT_LOCATOR_TYPE = By.XPATH

	@classmethod
	def click_button(cls, driver, locator_data, by_locator_type=DEFAULT_LOCATOR_TYPE):
		button = cls.get_web_element(driver, locator_data, by_locator_type)
		try:
			button.click()
		except ElementNotInteractableException:
			ActionChains(driver).move_to_element(button).click().perform()

	@classmethod
	def get_web_element(cls, driver, locator_data, by_locator_type=DEFAULT_LOCATOR_TYPE):
		return driver.find_element(by_locator_type, locator_data)

	@classmethod
	def enter_message_to_text_box(cls, driver, locator_data, *messages, by_locator_type=DEFAULT_LOCATOR_TYPE):
		text_box = cls.get_web_element(driver, locator_data, by_locator_type)
		text_box.clear()
		for message in messages:
			text_box.send_keys(message)

	@classmethod
	def select_from_list_of_elements(cls, driver, required_index, locator_data, locator_type=DEFAULT_LOCATOR_TYPE):
		elements_list = cls.get_list_of_elements(driver, locator_data, locator_type)
		required_element = elements_list[required_index]
		required_element.click()

	@classmethod
	def select_check_box(cls, driver, locator_data, by_locator_type=DEFAULT_LOCATOR_TYPE):
		check_box = cls.get_web_element(driver, locator_data, by_locator_type)
		if not check_box.is_selected():
			check_box.click()

	@classmethod
	def get_list_of_elements(cls, driver, locator_data, by_locator_type=DEFAULT_LOCATOR_TYPE):
		return driver.find_elements(by_locator_type, locator_data)

	@classmethod
	def double_click_option(cls, driver, locator_data, by_locator_type=DEFAULT_LOCATOR_TYPE):
		option = cls.get_web_element(driver, locator_data, by_locator_type)
		ActionChains(driver).move_to_element(option).click(option).perform()
