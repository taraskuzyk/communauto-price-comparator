import pytest
from trips import *
from main import INVOICE_STRING

lines = INVOICE_STRING.split("\n")

ROUNDING_ERROR_TOLERANCE = 0.5


def is_equal_within_tolerance(a: float, b: float) -> bool:
    """a and b are non-zero floats"""
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative floats")
    return get_min_with_error(a) <= b <= get_max_with_error(a)


def get_min_with_error(num: float) -> float:
    return num - ROUNDING_ERROR_TOLERANCE


def get_max_with_error(num: float) -> float:
    return num + ROUNDING_ERROR_TOLERANCE


test_trips = []
for line in lines:
    try:
        trip = Trip.from_invoice_line(line)
    except ValueError:
        continue
    test_trips.append(trip)


invoice_line = "5881 415324 05/01 15:26 05/01 16:42 0 1.23 $21.30 7 $0.00 $0.00 $1.00 CDW $22.30 FLEX $0.00"

test_trip = Trip(
    hours=1.23,
    kilometers=7,
    days=0
)

test_plan = Plan(
    name="Test Plan",
    hourly_rate=15.0,
    minute_rate=0.45,
    daily_rate=50,
    kilometer_rate=0.2,
    kilometers_included=100
)


def test_get_trip_from_invoice_line():
    trip = Trip.from_invoice_line(invoice_line)
    assert test_trip.hours == trip.hours
    assert test_trip.kilometers == trip.kilometers
    assert test_trip.days == trip.days


def test_get_time_cost():
    cost = test_trip._get_time_cost(test_plan)
    assert is_equal_within_tolerance(cost, 21.3)


def test_get_distance_cost():
    cost = test_trip._get_distance_cost(test_plan)
    assert cost == 0


def test_get_invoice_cost_using_plan():
    cost = get_trips_cumulative_cost_using_plan(test_trips, test_plan)
    assert is_equal_within_tolerance(cost, 302.75)


