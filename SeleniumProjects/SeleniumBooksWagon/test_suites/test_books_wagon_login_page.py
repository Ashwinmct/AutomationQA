import pytest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from drivers.books_wagon_driver import BooksWagonDriver
from credentials import credentials as user_detail
from object_repository import constants
from utilities.event_listener import TestListener


@pytest.mark.usefixtures('get_driver_object')
class TestBooksWagonLoginPage(object):

	@pytest.fixture(autouse=True)
	def open_login_page(self, get_driver_object):
		global driver
		driver = get_driver_object
		driver = EventFiringWebDriver(driver, TestListener())
		driver.get(constants.BOOKS_WAGON_URL)

	def test_login_to_books_wagon_using_valid_credentials(self):
		BooksWagonDriver.login(driver, email_id=user_detail.EMAIL_ID, password=user_detail.PASSWORD)
		assert driver.current_url, constants.USER_ACCOUNT_PAGE_URL
		BooksWagonDriver.log_out(driver)

	def test_log_out_option(self):
		BooksWagonDriver.login(driver, email_id=user_detail.EMAIL_ID, password=user_detail.PASSWORD)
		BooksWagonDriver.log_out(driver)
		assert driver.current_url == constants.LOGIN_PAGE_URL
