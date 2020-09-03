from make_my_trip_drivers.exceptions import MakeMyTripException
from make_my_trip_drivers.options import FlightType, FlightFilterOptions
from make_my_trip_page_objects.make_my_trip_search_results_page import MakeMyTripSearchResultsPage


class MakeMyTripSearchResultsPageDriver(object):

	@classmethod
	def get_search_results(cls, driver):
		try:
			search_results = MakeMyTripSearchResultsPage(driver=driver)
			return search_results
		except MakeMyTripException as exception:
			print(exception.exception_type.value)

	@classmethod
	def print_available_flights_count(cls, search_results):
		departure_flights = search_results.get_flights_details_list(FlightType.DEPARTURE_FLIGHTS)
		return_flights = search_results.get_flights_details_list(FlightType.RETURN_FLIGHTS)
		print(
			"Available flights:\n Departure Flights Available: %d \n Return Flights Available: %d \n "
			"Total "
			"Flights Available: %d " % (
				len(departure_flights), len(return_flights), (len(departure_flights) + len(return_flights))))

	@classmethod
	def apply_filters(cls, search_results):
		search_results.add_filter(FlightFilterOptions.ONE_STOP)
		search_results.add_filter(FlightFilterOptions.NON_STOP)

	@classmethod
	def get_flight_price(cls, flight):
		flight_details = flight.text.split('\n')
		return flight_details[-1]
