import unittest
import datetime
from timeutilities import Time
from time import sleep


class TimeTests(unittest.TestCase):
    def test_to_seconds(self):
        timer = Time(10, 5, 1)
        self.assertEqual(
            timer.to_seconds(),
            10 + (5 * 60) + (60 * 60),
            "Check accurate seconds conversions",
        )

    def test_from_seconds(self):
        timer2 = Time(10, 5, 1)
        timer1 = Time.from_seconds(10 + (5 * 60) + (60 * 60))

        self.assertEqual(
            timer1, timer2, "Check if time from seconds and time itself match"
        )

    def test_add_time(self):
        self.assertEqual(Time(300) + Time(300), Time(600), "Adding to times together")
        self.assertEqual(Time(10, 2), Time(0, 2) + 10, "Adding seconds to time")

    def test_ticks(self):
        start = Time()
        start.tick()
        self.assertEqual(start, Time(1), "1 tick is 1 second")
        start.tick()
        self.assertEqual(start, Time(2), "2 ticks is 2 seconds")

    def test_timed_ticks(self):
        start = Time()
        start.tick(True)
        sleep(10)
        start.end_tick()
        self.assertEqual(start, Time(10), "Timed ticks")

    def test_comparisons(self):
        self.assertGreater(Time(0, 1), Time(59))
        self.assertLess(Time(0, 1), Time(61))

    def test_subtract_time(self):
        self.assertEqual(
            Time(500), Time(900) - Time(400), "Subtracting times to gether"
        )
        self.assertEqual(Time(0, 5), Time(10, 5) - 10, "Subtracting seconds from time")

    def test_time_equality(self):
        self.assertEqual(Time(10, 1), Time(70))

    def test_to_time(self):
        timer = Time(10, 10, 12)
        self.assertEqual(
            timer.to_time(), datetime.time(12, 10, 10), "Converting to datetime"
        )


if __name__ == "__main__":
    unittest.main()
