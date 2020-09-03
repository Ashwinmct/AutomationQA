from selenium.webdriver.common.keys import Keys

from page_objects.bookswagon_site import BooksWagon
from drivers.ui_driver import UIDriver
from object_repository import constants


class BooksWaggonHomePage(BooksWagon):

	def click_login_button(self):
		UIDriver.click_button(self.driver, constants.HOME_PAGE_LOGIN_BUTTON)

	def click_user_account_button(self):
		UIDriver.click_button(self.driver, constants.HOME_PAGE_USER_ACCOUNT_BUTTON)

	def select_logout_option(self):
		self.click_user_account_button()
		UIDriver.click_button(self.driver, constants.LOG_OUT_OPTION)

	def search(self, book_name):
		UIDriver.enter_message_to_text_box(self.driver, constants.SEARCH_BOX_XPATH, book_name, Keys.ENTER)

	def open_best_sellers(self):
		UIDriver.click_button(self.driver, constants.BEST_SELLERS)

	def go_to_wish_list(self):
		self.click_user_account_button()
		UIDriver.click_button(self.driver, constants.WISH_LIST_OPTION)
