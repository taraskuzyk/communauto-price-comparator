from typing import List

from definitions import VERY_LARGE_NUMBER, MINUTES_IN_AN_HOUR


class Plan:
    def __init__(self, name: str, hourly_rate: float, daily_rate: float,
                 kilometer_rate: float, minute_rate=None, kilometers_included=0, x_mark_kilometer=VERY_LARGE_NUMBER,
                 x_mark_kilometer_rate=0.0, has_four_hour_rule=False):
        self.name = name
        self.hourly_rate = hourly_rate
        self.minute_rate = minute_rate if minute_rate is not None else hourly_rate / MINUTES_IN_AN_HOUR
        self.daily_rate = daily_rate
        self.kilometer_rate = kilometer_rate
        self.kilometers_included = kilometers_included
        self.x_mark_kilometer_rate = x_mark_kilometer_rate
        self.x_mark_kilometer = x_mark_kilometer
        self.has_four_hour_rule = has_four_hour_rule

    def get_number_of_minutes_until_hourly_rate(self):
        return int(self.hourly_rate / self.minute_rate)


PLANS = dict(
    FLEX=Plan(
        name="Flex",
        hourly_rate=15.0,
        minute_rate=0.45,
        daily_rate=50,
        kilometer_rate=0.2,
        kilometers_included=100,
    ),

    FLEX_OPEN=Plan(
        name="Flex Open",
        hourly_rate=14.0,
        daily_rate=50,
        minute_rate=0.41,
        kilometer_rate=0.2,
        kilometers_included=100
    ),

    FLEX_VALUE=Plan(
        name="Flex Value",
        hourly_rate=3.95,
        daily_rate=27.65,
        kilometer_rate=0.39,
        x_mark_kilometer=50,
        x_mark_kilometer_rate=0.15
    ),

    FLEX_VALUE_PLUS=Plan(
        name="Flex Value Plus",
        hourly_rate=3.55,
        daily_rate=24.85,
        kilometer_rate=0.35,
        x_mark_kilometer=50,
        x_mark_kilometer_rate=0.15,
        has_four_hour_rule=True
    ),

    FLEX_VALUE_EXTRA=Plan(
        name="Flex Value Extra",
        hourly_rate=2.95,
        daily_rate=20.65,
        kilometer_rate=0.25,
        x_mark_kilometer=50,
        x_mark_kilometer_rate=0.15,
        has_four_hour_rule=True
    )

)

