from credentials import credentials
from page_objects.books_wagon_login_page import BooksWagonLoginPage
from page_objects.bookswagon_home_page import BooksWaggonHomePage
from page_objects.bookswagon_user_account_page import BooksWagonUserAccountPage


class BooksWagonDriver(object):
	@classmethod
	def login(cls, driver, email_id=credentials.EMAIL_ID, password=credentials.PASSWORD):
		home_page = BooksWaggonHomePage(driver)
		home_page.click_login_button()
		login_page = BooksWagonLoginPage(driver)
		login_page.enter_email(email_id)
		login_page.enter_password(password)
		login_page.click_login_button()

	@classmethod
	def log_out(cls, driver):
		user_account_page = BooksWagonUserAccountPage(driver)
		user_account_page.click_home_button()
		BooksWaggonHomePage(driver).select_logout_option()

	@classmethod
	def clear_wish_list(cls, driver):
		home_page = BooksWaggonHomePage(driver)
		home_page.go_to_wish_list()
		wish_list = BooksWagonUserAccountPage(driver)
		if not wish_list.is_empty():
			wish_list.remove_all()
		wish_list.go_to_home_page()

	@classmethod
	def clear_cart(cls, driver):
		home_page = BooksWaggonHomePage(driver)
		home_page.go_to_cart()
		home_page.remove_books_from_cart()
