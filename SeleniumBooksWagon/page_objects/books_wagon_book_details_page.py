from drivers.ui_driver import UIDriver
from object_repository import constants
from page_objects.bookswagon_site import BooksWagon


class BooksWagonBookDetailsPage(BooksWagon):
	def click_on_buy_now_button(self):
		UIDriver.click_button(self.driver, constants.BUY_NOW_BUTTON_XPATH)
