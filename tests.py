"""
tests
"""

import datetime
import unittest

from main import get_WeekNum_and_DayOfWeek


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_divmod(self):
        d = datetime.date(2023, 11, 7)
        divmod_ = divmod(d.day, 7)  # 日付を７で割って商と余りを取得
        self.assertEqual(divmod_[0], 1)
        self.assertEqual(divmod_[1], 0)

        d = datetime.date(2023, 11, 8)
        divmod_ = divmod(d.day, 7)
        self.assertEqual(divmod_[0], 1)
        self.assertEqual(divmod_[1], 1)

    def test_something1(self):
        d = datetime.date(2023, 11, 7)
        t = get_WeekNum_and_DayOfWeek(d)
        self.assertEqual(t, (1, "火"))

    def test_something2(self):
        d = datetime.date(2023, 11, 8)
        t = get_WeekNum_and_DayOfWeek(d)
        self.assertEqual(t, (2, "水"))

    def test_something3(self):
        d = datetime.date(2023, 12, 5)
        t = get_WeekNum_and_DayOfWeek(d)
        self.assertEqual(t, (1, "火"))

    def test_something4(self):
        d = datetime.date(2023, 11, 5)
        t = get_WeekNum_and_DayOfWeek(d)
        self.assertEqual(t, (1, "日"))

    def test_something5(self):
        d = datetime.date(2023, 11, 28)
        t = get_WeekNum_and_DayOfWeek(d)
        self.assertEqual(t, (4, "火"))

        d = datetime.date(2023, 11, 29)
        t = get_WeekNum_and_DayOfWeek(d)
        self.assertEqual(t, (5, "水"))

        d = datetime.date(2023, 11, 30)
        t = get_WeekNum_and_DayOfWeek(d)
        self.assertEqual(t, (5, "木"))

        d = datetime.date(2023, 12, 1)
        t = get_WeekNum_and_DayOfWeek(d)
        self.assertEqual(t, (1, "金"))


if __name__ == "__main__":
    unittest.main()
