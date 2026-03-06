from unittest import TestCase
from City import City


class TestCity(TestCase):
    # test average_monthly
    def test_average_monthly_1(self):
        test_city = City("Test1.csv", "9/1/2025")
        self.assertEqual(2.0, test_city.average_monthly(9, 2025))

    def test_average_monthly_2(self):
        test_city = City("Test2.csv", "9/1/2025")
        self.assertEqual(10.0, test_city.average_monthly(9, 2025))

    # test average_weekly
    def test_average_weekly_1(self):
        test_city = City("Test1.csv", "9/1/2025")
        self.assertEqual(2.0, test_city.average_weekly(36, 2025))

    def test_average_weekly_2(self):
        test_city = City("Test2.csv", "9/1/2025")
        self.assertEqual(10.0, test_city.average_weekly(36, 2025))

    # test average_daily
    def test_average_daily_1(self):
        test_city = City("Test1.csv", "9/1/2025")
        self.assertEqual(2.0, test_city.average_daily(244, 2025))

    def test_average_daily_2(self):
        test_city = City("Test2.csv", "9/1/2025")
        self.assertEqual(10.0, test_city.average_daily(244, 2025))

    # test highest_recording
    def test_highest_recording_1(self):
        test_city = City("Test1.csv", "9/1/2025")
        self.assertEqual(3.0, test_city.highest_recording().value)

    def test_highest_recording_2(self):
        test_city = City("Test2.csv", "9/1/2025")
        self.assertEqual(10.0, test_city.highest_recording().value)

    # test lowest_recording
    def test_lowest_recording_1(self):
        test_city = City("Test1.csv", "9/1/2025")
        self.assertEqual(1.0, test_city.lowest_recording().value)

    def test_lowest_recording_2(self):
        test_city = City("Test2.csv", "9/1/2025")
        self.assertEqual(10.0, test_city.lowest_recording().value)

    # test readings_exeeding_health_standards
    def test_readings_exeeding_health_standards_1(self):
        test_city = City("Test1.csv", "9/1/2025")
        self.assertEqual(3, len(test_city.readings_exeeding_health_standards(0.0)))

    def test_readings_exeeding_health_standards_2(self):
        test_city = City("Test1.csv", "9/1/2025")
        self.assertEqual(1, len(test_city.readings_exeeding_health_standards(2.5)))
