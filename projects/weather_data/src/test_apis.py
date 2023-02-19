import unittest
import json
from weather_app import app


class TestWeatherRecords(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_weather_records(self):
        response = self.app.get("/api/weather")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(isinstance(data, list))

    def test_get_weather_records_filter_by_date(self):
        response = self.app.get("/api/weather?date=2019-01-01")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(isinstance(data, list))
        self.assertTrue(all(row["date"] == "2019-01-01" for row in data))

    def test_get_weather_records_filter_by_station(self):
        response = self.app.get("/api/weather?station=ABC123")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(isinstance(data, list))
        self.assertTrue(all(row["station"] == "ABC123" for row in data))

    def test_get_weather_records_pagination(self):
        response = self.app.get("/api/weather?page=2&page_size=20")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 20)


class TestWeatherStats(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_weather_stats(self):
        response = self.app.get("/api/weather/stats")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(isinstance(data, list))

    def test_get_weather_stats_filter_by_year(self):
        response = self.app.get("/api/weather/stats?year=2019")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(isinstance(data, list))
        self.assertTrue(all(row["year"] == 2019 for row in data))

    def test_get_weather_stats_filter_by_station(self):
        response = self.app.get("/api/weather/stats?station=ABC123")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(isinstance(data, list))
        self.assertTrue(all(row["station"] == "ABC123" for row in data))

    def test_get_weather_stats_pagination(self):
        response = self.app.get("/api/weather/stats?page=2&page_size=1")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 0)


if __name__ == "__main__":
    unittest.main()
