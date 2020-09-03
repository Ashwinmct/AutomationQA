from drivers.ui_driver import UIDriver
from page_objects.bookswagon_site import BooksWagon
from object_repository import constants


class BooksWagonLoginPage(BooksWagon):

	def enter_email(self, email_id):
		UIDriver.enter_message_to_text_box(self.driver, constants.LOGIN_EMAIL_ID_XPATH, email_id)

	def enter_password(self, password):
		UIDriver.enter_message_to_text_box(self.driver, constants.LOGIN_PASSWORD_XPATH, password)

	def click_login_button(self):
		UIDriver.click_button(self.driver, constants.LOGIN_PAGE_LOG_IN_BUTTON)
