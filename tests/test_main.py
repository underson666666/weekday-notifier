"""
tests
"""

from main import *
import datetime

import pytest

from main import get_WeekNum_and_DayOfWeek


class TestMain:
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @pytest.mark.parametrize(
        "year, month, day, expect",
        [(2023, 11, 7, (1, 0)), (2023, 11, 8, (1, 1))],
    )
    def test_divmod(self, year, month, day, expect):
        d = datetime.date(year, month, day)
        divmod_ = divmod(d.day, 7)  # 日付を７で割って商と余りを取得
        assert divmod_[0] == expect[0]
        assert divmod_[1] == expect[1]

    @pytest.mark.parametrize(
        "year, month, day, numofweek, dayofweek",
        [
            (2023, 11, 7, 1, "火"),
            (2023, 11, 8, 2, "水"),
            (2023, 12, 5, 1, "火"),
            (2023, 11, 5, 1, "日"),
            (2023, 11, 28, 4, "火"),
            (2023, 11, 29, 5, "水"),
            (2023, 11, 30, 5, "木"),
            (2023, 12, 1, 1, "金"),
        ],
    )
    def test_something1(self, year, month, day, numofweek, dayofweek):
        d = datetime.date(year, month, day)
        t = get_WeekNum_and_DayOfWeek(d)
        assert t == (numofweek, dayofweek)
