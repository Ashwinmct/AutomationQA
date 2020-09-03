import pytest
from datetime import date
from selenium.webdriver.common.by import By
from make_my_trip_drivers.exceptions import MakeMyTripException
from object_repository import constants
from make_my_trip_drivers.home_page_driver import MakeMyTripDriver
from make_my_trip_drivers.options import FlightType, ReflectedFlightType
from make_my_trip_drivers.search_results_page_driver import MakeMyTripSearchResultsPageDriver as searchPage
from utilities.screenshot import ScreenShot


@pytest.mark.usefixtures('get_driver_object')
class TestMakeMyTrip:
	@pytest.fixture(autouse=True)
	def get_driver_object(self, get_driver_object):
		global driver
		driver = get_driver_object
		self.__load__flight_details()

	@pytest.mark.xfail(raises=MakeMyTripException)
	def test_search_flights_in_selenium(self):
		assert self.assert_test_values(driver.title, constants.SEARCH_PAGE_TITLE, 'load search test')

	@pytest.mark.xfail(raises=MakeMyTripException)
	def test_search_page(self):
		search_results = searchPage.get_search_results(driver)
		searchPage.print_available_flights_count(search_results)
		searchPage.apply_filters(search_results)
		print("Available flights after filtering")
		searchPage.print_available_flights_count(search_results)

	@pytest.mark.xfail(raises=MakeMyTripException)
	def test_search_page_reflecting_values(self):

		search_results = searchPage.get_search_results(driver)
		searchPage.apply_filters(search_results)
		selected_departure_flight_value = searchPage.get_flight_price(
			search_results.select_flight(FlightType.DEPARTURE_FLIGHTS))
		selected_return_flight_value = searchPage.get_flight_price(
			search_results.select_flight(FlightType.RETURN_FLIGHTS))
		reflected_departure_flight_price = search_results.get_reflected_flight_price(
			ReflectedFlightType.DEPARTURE_FLIGHTS)
		reflected_return_flight_price = search_results.get_reflected_flight_price(ReflectedFlightType.RETURN_FLIGHTS)
		assert self.assert_test_values(selected_departure_flight_value, reflected_departure_flight_price,
		                               'wrong reflected values') and self.assert_test_values(
			selected_return_flight_value, reflected_return_flight_price, 'wrong reflected values')

	@pytest.mark.xfail(raises=MakeMyTripException)
	def test_search_page_total_value(self):
		search_results = searchPage.get_search_results(driver)
		searchPage.apply_filters(search_results)
		selected_departure_flight_value = searchPage.get_flight_price(
			search_results.select_flight(FlightType.DEPARTURE_FLIGHTS))
		selected_return_flight_value = searchPage.get_flight_price(
			search_results.select_flight(FlightType.RETURN_FLIGHTS))
		reflected_total_value = (driver.find_element(By.XPATH, constants.REFLECTED_TOTAL_VALUE)).text
		assert self.assert_test_values(selected_departure_flight_value + selected_return_flight_value,
		                               reflected_total_value,
		                               'wrong total values')

	def __load__flight_details(self):
		required_return_date = date.today().day + 7
		MakeMyTripDriver.load_search(driver=driver, from_location=constants.FROM_LOCATION_REQUIRED,
		                             to_location=constants.REQUIRED_TO_LOCATION, return_date=required_return_date)

	def assert_test_values(self, expected_value, exact_value, failure_detail):
		if not expected_value == exact_value:
			ScreenShot.take_screen_shot(driver, failure_detail)
			return False
		return True
