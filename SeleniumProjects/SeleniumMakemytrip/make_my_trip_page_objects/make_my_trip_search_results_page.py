from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from make_my_trip_drivers.exceptions import MakeMyTripException
from make_my_trip_page_objects.make_my_trip import MakeMyTrip
from object_repository import constants


class MakeMyTripSearchResultsPage(MakeMyTrip):
	DEFAULT_INDEX = 0
	LAST_INDEX = -1

	def __init__(self, driver):
		MakeMyTrip.__init__(self, driver)
		self.__check_results_loading()

	def get_flights_details_list(self, flight_type):
		flights_list = self.driver.find_elements(By.XPATH, flight_type.value)
		if flight_type == constants.DEPARTURE_FLIGHTS_LIST_XPATH:
			flights_list = flights_list.pop(self.DEFAULT_INDEX)
		return flights_list

	def add_filter(self, filter_option):
		option = self.driver.find_element(By.XPATH, filter_option.value)
		self.click_option(option)

	def select_flight(self, flight_type, required_flight_index=LAST_INDEX):
		flights_list = self.get_flights_details_list(flight_type)
		required_flight = flights_list[required_flight_index]
		self.click_option(required_flight)
		return required_flight

	def get_reflected_flight_price(self, flight_type):
		return self.driver.find_element(By.XPATH, flight_type.value).text

	def __check_results_loading(self, status_flag=DEFAULT_INDEX):
		try:
			self.driver.find_element(By.XPATH, constants.SEARCH_RESULTS_AVAILABILITY)
		except NoSuchElementException:
			if status_flag != self.DEFAULT_INDEX:
				raise MakeMyTripException(MakeMyTripException.ExceptionType.NO_FLIGHTS_FOUND)
			self.driver.refresh()
			self.__check_results_loading(status_flag+1)
		except TimeoutException:
			self.driver.refresh()
			self.driver.set_page_load_timeout(20)
