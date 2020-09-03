import time

import pytest

from drivers.books_wagon_driver import BooksWagonDriver
from exceptions.books_wagon_exception import BooksWagonException
from object_repository import constants
from page_objects.books_wagon_book_details_page import BooksWagonBookDetailsPage
from page_objects.bookswagon_home_page import BooksWaggonHomePage
from page_objects.bookswagon_user_account_page import BooksWagonUserAccountPage


@pytest.mark.usefixtures('get_driver_object')
class TestBooksWagonCart(object):
	quantity = 2

	@pytest.fixture(autouse=True)
	def open_login_page(self, get_driver_object):
		global driver
		driver = get_driver_object
		driver.get(constants.BOOKS_WAGON_URL)
		BooksWagonDriver.login(driver)
		yield
		BooksWagonDriver.log_out(driver)

	@pytest.mark.xfail(raises=BooksWagonException)
	def test_search_and_selecting_the_book(self):
		home_page = BooksWaggonHomePage(driver)
		home_page.search('Shiva triology')
		home_page.select_books_from_results('Shiva triology')
		book_page = BooksWagonBookDetailsPage(driver)
		book_page.click_on_buy_now_button()

	def test_book_wish_list(self):
		BooksWagonDriver.clear_cart(driver)
		BooksWagonDriver.clear_wish_list(driver)
		home_page = BooksWaggonHomePage(driver)
		home_page.open_best_sellers()
		home_page.select_below_100_rs()
		home_page.add_cheapest_book_to_wish_list()
		wish_list = BooksWagonUserAccountPage(driver)
		wish_list.select_all()
		wish_list.buy_selected()
		wish_list.go_to_cart()
		home_page.enter_quantity_to_cart(self.quantity)
		home_page.click_place_order()
		home_page.go_to_home_page()

	def test_selected_same_book_is_added_to_the_wish_list_or_not(self):
		BooksWagonDriver.clear_wish_list(driver)
		home_page = BooksWaggonHomePage(driver)
		home_page.open_best_sellers()
		home_page.select_below_100_rs()
		time.sleep(home_page.DEFAULT_WAIT)
		cheapest_book_name = home_page.get_best_seller_cheapest_book_name()
		home_page.add_cheapest_book_to_wish_list()
		book_in_wish_list_name = BooksWagonUserAccountPage(driver).get_first_book_name()
		assert book_in_wish_list_name == cheapest_book_name
