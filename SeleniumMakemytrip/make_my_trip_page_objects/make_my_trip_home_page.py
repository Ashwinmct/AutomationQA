from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from make_my_trip_page_objects.make_my_trip import MakeMyTrip
from object_repository import constants


class MakeMyTripHomePage(MakeMyTrip):
	def __init__(self, driver):
		MakeMyTrip.__init__(self, driver)
		self.__load_home_page()

	def __load_home_page(self):
		self.driver.get(constants.HOME_URL)
		self.driver.set_page_load_timeout(20)

	#to choose flight in the travel options
	def select_flight_option(self):
		flight_option = self.driver.find_element(By.XPATH, constants.FLIGHT_OPTION_XPATH)
		self.click_option(flight_option)

	#to select and click round trip option
	def select_round_trip(self):
		(self.driver.find_element(By.XPATH, constants.ROUND_TRIP_OPTION_XPATH)).click()

	def select_from_location(self, location):
		self.__city_selector(constants.FROM_OPTION_XPATH, constants.FROM_LOCATION_INPUT_XPATH,
		                     constants.SUGGESTED_FROM_CITIES_XPATH, location)

	def select_to_location(self, to_location):
		self.__city_selector(constants.TO_LOCATION_XPATH, constants.TO_LOCATION_INPUT_XPATH,
		                     constants.SUGGESTED_TO_CITIES_XPATH, to_location)

	#select the city for from or to options
	def __city_selector(self, location_option_xpath, option_input_xpath, suggested_city_xpath, location):
		location_box = self.driver.find_element(By.XPATH, location_option_xpath)
		self.click_option(location_box)
		location_input = self.driver.find_element(By.XPATH, option_input_xpath)
		location_input.send_keys(location)
		suggested_cities = self.driver.find_elements(By.XPATH, suggested_city_xpath)
		for city in suggested_cities:
			if location.lower() in city.text.lower():
				self.click_option(city)
				return

	def select_departure_date(self, day):
		departure_option = self.driver.find_element(By.XPATH, constants.DEPARTURE_OPTION_XPATH)
		self.click_option(departure_option)
		available_dates = self.driver.find_elements(By.XPATH, constants.DEPARTURE_DATES_XPATH)
		for date in available_dates:
			if date.text.__eq__(day):
				self.click_option(date)
				return

	def click_search_button(self):
		try:
			self.click_option(self.driver.find_element(By.XPATH, constants.SEARCH_OPTION_XPATH))
			self.driver.set_page_load_timeout(20)
		except TimeoutException:
			self.driver.set_page_load_timeout(20)
