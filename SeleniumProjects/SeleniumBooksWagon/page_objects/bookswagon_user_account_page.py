from selenium.common.exceptions import NoSuchElementException

from object_repository import constants
from drivers.ui_driver import UIDriver
from page_objects.bookswagon_site import BooksWagon


class BooksWagonUserAccountPage(BooksWagon):
	def click_home_button(self):
		UIDriver.click_button(self.driver, constants.HOME_BUTTON_XPATH)

	def buy_first_book(self):
		UIDriver.click_button(self.driver, constants.BUY_WISH_LIST_BOOKS_XPATH)

	def select_all(self):
		UIDriver.select_check_box(self.driver, constants.SELECT_ALL_BOOKS)

	def buy_selected(self):
		UIDriver.double_click_option(self.driver, constants.BUY_SELECTED_BOOKS)

	def is_empty(self):
		try:
			UIDriver.get_web_element(self.driver, constants.SELECT_ALL_BOOKS)
			return False
		except NoSuchElementException:
			return True

	def remove_all(self):
		self.select_all()
		UIDriver.click_button(self.driver, constants.REMOVE_ALL_BUTTON)

	def get_first_book_name(self):
		return (UIDriver.get_web_element(self.driver, constants.BOOK_IN_WISH_LIST)).text
