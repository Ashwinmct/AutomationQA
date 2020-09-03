from enum import Enum
from object_repository import constants


class FlightFilterOptions(Enum):
	ONE_STOP = constants.ONE_STOP_XPATH
	NON_STOP = constants.NON_STOP_XPATH


class FlightType(Enum):
	DEPARTURE_FLIGHTS = constants.DEPARTURE_FLIGHTS_LIST_XPATH
	RETURN_FLIGHTS = constants.RETURN_FLIGHTS_LIST_XPATH

class ReflectedFlightType(Enum):
	DEPARTURE_FLIGHTS = constants.REFLECTED_DEPARTURE_FLIGHT_PRICE
	RETURN_FLIGHTS = constants.RETURN_FLIGHTS_LIST_XPATH
