import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from drivers.ui_driver import UIDriver
from exceptions.books_wagon_exception import BooksWagonException
from object_repository import constants


class BooksWagon(object):
	DEFAULT_WAIT = 5
	BOOK_INDEX = 0
	EMPTY = 0

	def __init__(self, driver):
		self.driver = driver

	def remove_books_from_cart(self):
		try:
			while True:
				removable_books = UIDriver.get_list_of_elements(self.driver, constants.REMOVE_LIST_CLASS,
				                                                By.CLASS_NAME)
				if len(removable_books) == self.EMPTY:
					break
				ActionChains(self.driver).move_to_element(removable_books[self.BOOK_INDEX]).click(
					removable_books[self.BOOK_INDEX]).perform()
				time.sleep(self.DEFAULT_WAIT)
		except NoSuchElementException:
			UIDriver.click_button(self.driver, constants.CONTINUE_SHOPPING)
		finally:
			time.sleep(self.DEFAULT_WAIT)

	def go_to_home_page(self):
		UIDriver.click_button(self.driver, constants.HOME_PAGE_BUTTON)

	def go_to_cart(self):
		UIDriver.click_button(self.driver, constants.CART_ICON_XPATH)
		self.switch_to_cart()

	def enter_quantity_to_cart(self, quantity):
		UIDriver.enter_message_to_text_box(self.driver, constants.QUANTITY_BOX, quantity)

	def click_place_order(self):
		UIDriver.click_button(self.driver, constants.PLACE_ORDER)

	def add_cheapest_book_to_wish_list(self):
		time.sleep(self.DEFAULT_WAIT)
		UIDriver.select_from_list_of_elements(self.driver, self.BOOK_INDEX, constants.BEST_SELLING_BOOKS_XPATH)

	def select_below_100_rs(self):
		UIDriver.click_button(self.driver, constants.BELOW_100_RS)

	def select_books_from_results(self, book_name):
		result_books = self.driver.find_elements(By.XPATH, '//*[@id="listSearchResult"]/div')
		for book in result_books:
			if book_name.lower() in book.text.lower():
				book.click()
		else:
			raise BooksWagonException(BooksWagonException.ExceptionType.NO_BOOK_FOUND)

	def get_best_seller_cheapest_book_name(self):
		return (UIDriver.get_list_of_elements(self.driver, constants.CHEAPEST_BOOK_IN_BEST_SELLER_PAGE_NAME_XPATH))[
			self.BOOK_INDEX].text

	def switch_to_cart(self):
		cart_frame = WebDriverWait(self.driver, 10).until(
			ec.presence_of_element_located((By.XPATH, constants.CART_FRAME_XPATH)))
		self.driver.switch_to.frame(cart_frame)
