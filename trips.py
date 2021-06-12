from typing import List
from plans import Plan, PLANS
from definitions import MINUTES_IN_AN_HOUR


class Trip:
    def __init__(self, days: int, hours: float, kilometers: int):
        self.days = days
        self.hours = hours
        self.kilometers = kilometers

    @classmethod
    def from_invoice_line(cls, line: str):
        car_number, user_number, start_date, start_time, end_date, end_time, number_of_days, number_of_hours, \
            cost, kilometers, distance_cost, booking_fee, other_fee, description, total_cost, rate_applied, \
            purchases = line.split()

        return cls(
            kilometers=int(kilometers),
            days=int(number_of_days),
            hours=float(number_of_hours),
        )

    def get_cost_using_plan(self, plan: Plan) -> float:
        this_plan_cost = self._get_cost_using_plan(plan)
        if plan.has_four_hour_rule:
            flex_open_cost = self._get_cost_using_plan(PLANS["FLEX_OPEN"])  # accessing dict like this violates SRP
            return min(this_plan_cost, flex_open_cost)

        return this_plan_cost

    def _get_cost_using_plan(self, plan: Plan) -> float:
        return self._get_time_cost(plan) + self._get_distance_cost(plan)

    def _get_distance_cost(self, plan: Plan):
        if self.kilometers <= plan.x_mark_kilometer:
            if self.kilometers <= plan.kilometers_included:
                return 0
            else:
                return (self.kilometers - plan.kilometers_included) * plan.kilometer_rate
        else:
            return (self.kilometers - plan.x_mark_kilometer) * plan.x_mark_kilometer_rate + \
                   plan.x_mark_kilometer * plan.hourly_rate

    def _get_time_cost(self, plan: Plan) -> float:
        if self.days > 0:
            return plan.daily_rate * self.days

        time_in_last_hour = self.hours % 1
        if self.hours % 1 < plan.get_number_of_minutes_until_hourly_rate() / MINUTES_IN_AN_HOUR:
            last_hour_cost = time_in_last_hour * MINUTES_IN_AN_HOUR * plan.minute_rate
            assert last_hour_cost < plan.hourly_rate
        else:
            last_hour_cost = plan.hourly_rate

        return last_hour_cost + int(self.hours) * plan.hourly_rate


# TODO: clarify quick round trip cost


def get_trips_cumulative_cost_using_plan(trips: List[Trip], plan: Plan) -> float:
    invoice_sum = 0
    for trip in trips:  # TODO: could probably use reduce here
        trip_cost = trip.get_cost_using_plan(plan)
        invoice_sum += trip_cost
    return invoice_sum
