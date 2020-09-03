import time
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver import ActionChains


class MakeMyTrip:
	DEFAULT_TIME_OUT = 5

	def __init__(self, driver):
		self.driver = driver

	def click_option(self, option, time_out=DEFAULT_TIME_OUT):
		try:
			option.click()
		except ElementClickInterceptedException or StaleElementReferenceException:
			ActionChains(self.driver).move_to_element(option).click(option).perform()
		finally:
			time.sleep(time_out)
