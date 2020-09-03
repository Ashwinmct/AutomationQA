import pytest
import time
import enum
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from builtins import staticmethod


class Sites(enum.Enum):
	GOOGLE = 'https://www.google.co.in/'
	GEEKS = 'https://www.geeksforgeeks.org/'
	PYTHON = 'https://www.python.org/'
	DEMO_RIGHT_CLICK = 'http://www.http.swisnl.github.io/jQuery_contextMenu/demo.htm/'
	DEMO_DRAG_AND_DROP = 'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
	DEMO_DOUBLE_CLICK = 'http://www.testautomationpractice.blogspot.com/'
	DEMO_ALERT = 'http://www.demo.guru99.com/test/delete_customer.php'
	DEMO_POP_UP = 'http://www.demo.guru99.com/popup.php'
	DEMO_DATE_ENTER = "http://demo.guru99.com/test/"
	DEMO_DATE_PICKER = 'https://jqueryui.com/datepicker/#date-range'


class TestSeleniumExample:
	@pytest.fixture
	def get_driver_object(self):
		global driver
		driver = webdriver.Chrome(executable_path=r"C:\\Users\\VIGNESH\\Drivers\\chromedriver_win32\\chromedriver.exe")
		driver.maximize_window()
		yield driver
		driver.close()
		driver.quit()

	def test_driver_connection_to_required_website(self, get_driver_object):
		driver.get(Sites.PYTHON.value)
		assert "Python" in driver.title
		assert Sites.PYTHON.value == driver.current_url

	def test_find_an_element_in_connected_website(self, get_driver_object):
		driver.get(Sites.PYTHON.value)
		element = self.__get_search_element(driver)
		self.__enter_message_to_element(element, message='pycon')
		assert "No results found." not in driver.page_source

	def test_browser_page_navigation(self, get_driver_object):
		url = Sites.GOOGLE.value
		driver.get(Sites.GOOGLE.value)
		element = self.__get_search_element(driver)
		self.__enter_message_to_element(element, message='AshwinMcp')
		forward_url = driver.current_url
		driver.back()
		assert url == driver.current_url
		driver.forward()
		assert forward_url == driver.current_url

	def test_for_explicit_wait(self, get_driver_object):
		driver.get(Sites.GOOGLE.value)
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

	def test_for_implicit_wait(self, get_driver_object):
		driver.implicitly_wait(10)
		driver.get(Sites.GOOGLE.value)
		self.__get_search_element(driver)

	def test_example_for_action_chain(self, get_driver_object):
		driver.get(Sites.GEEKS.value)
		element = driver.find_element_by_link_text("Courses")
		action = ActionChains(driver)
		action.click_and_hold(on_element=element)
		action.perform()

	def test_example_for_taking_screenshot(self, get_driver_object):
		driver.get(Sites.GOOGLE.value)
		time.sleep(10)
		driver.save_screenshot('screenshot.png')

	def test_for_mouse_right_click_option(self, get_driver_object):
		driver.get(Sites.DEMO_RIGHT_CLICK.value)
		button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
		actions = ActionChains(driver=driver)
		actions.context_click(button).perform()

	def test_for_mouse_drag_drop_option(self, get_driver_object):
		driver.get(Sites.DEMO_DRAG_AND_DROP.value)
		source_element = driver.find_element_by_xpath("//*[@id='box6']")
		target_element = driver.find_element_by_xpath("//*[@id='box106']")
		actions = ActionChains(driver=driver)
		actions.drag_and_drop(source_element, target_element).perform()
		
	def test_for_mouse_double_click_option(self, get_driver_object):
		driver.get(Sites.DEMO_DOUBLE_CLICK.value)
		button = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
		actions = ActionChains(driver=driver)
		actions.double_click(button).perform()
		driver.implicitly_wait(10)

	def test_example_for_alert_handling(self, get_driver_object):
		driver.get(Sites.DEMO_ALERT.value)
		driver.find_element(By.NAME, 'cusid').send_keys('54321')
		driver.find_element(By.NAME, 'submit').submit()
		alert_box = driver.switch_to.alert
		print(alert_box.text)
		alert_box.accept()

	def test_enter_date_in_calender_shown_in_the_website(self, get_driver_object):
		driver.get(Sites.DEMO_DATE_ENTER.value)
		date_box = driver.find_element(By.XPATH, "//form//input[@name='bdaytime']")
		date_box.send_keys('03082020')
		date_box.send_keys(Keys.TAB)
		date_box.send_keys('0620PM')

	def test_select_date_in_calender_shown_in_the_website(self, get_driver_object):
		expected_from_date_str = '08/20/2020'
		expected_to_date_str = '08/26/2020'
		expected_fr_date = '20'
		expected_to_date = '26'
		driver.get(Sites.DEMO_DATE_PICKER.value)
		driver.set_page_load_timeout(10)
		frame = driver.find_element(By.XPATH, "//*[@id='content']/iframe")
		driver.switch_to.frame(frame)
		from_date_picker = driver.find_element(By.XPATH, "//input[@id='from']")
		from_date_picker.click()
		time.sleep(5)
		from_month = driver.find_element(By.XPATH, "//div/select[@class='ui-datepicker-month']")
		selectable_from_months = Select(from_month)
		selectable_from_months.select_by_visible_text('Aug')
		from_day = driver.find_element_by_xpath(
			"//td[not(contains(@class,'ui-datepicker-month'))]/a[text()='" + expected_fr_date + "']")
		from_day.click()
		time.sleep(10)
		to_date_picker = driver.find_element_by_xpath("//input[@id='to']")
		to_date_picker.click()
		time.sleep(5)
		to_month = driver.find_element_by_xpath("//div/select[@class='ui-datepicker-month']")
		selected_to_month = Select(to_month)
		selected_to_month.select_by_visible_text("Aug")
		time.sleep(5)
		to_day = driver.find_element_by_xpath(
			"//td[not(contains(@class,'ui-datepicker-month'))]/a[text()='" + expected_to_date + "']")
		to_day.click()
		time.sleep(10)
		selected_from_date_str = from_date_picker.get_attribute('value')
		assert selected_from_date_str == expected_from_date_str
		selected_to_date_str = to_date_picker.get_attribute('value')
		assert selected_to_date_str == expected_to_date_str

	@staticmethod
	def __get_element_by_name(driver, name):
		return driver.find_element_by_name(name)

	def __get_search_element(self, driver):
		return self.__get_element_by_name(driver, 'q')

	def __enter_message_to_element(self, element, message):
		element.clear()
		element.send_keys(message)
		element.send_keys(Keys.RETURN)
