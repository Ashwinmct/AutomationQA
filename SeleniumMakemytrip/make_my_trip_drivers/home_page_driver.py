from make_my_trip_page_objects.make_my_trip_home_page import MakeMyTripHomePage


class MakeMyTripDriver:
	@classmethod
	def load_search(cls, driver, from_location, to_location, return_date):
		make_my_trip = MakeMyTripHomePage(driver)
		make_my_trip.select_flight_option()
		make_my_trip.select_round_trip()
		make_my_trip.select_from_location(from_location)
		make_my_trip.select_to_location(to_location)
		make_my_trip.select_departure_date(return_date)
		make_my_trip.click_search_button()
