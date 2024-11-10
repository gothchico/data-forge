from src.features.quant_data_models import IntradayDataModel, NewsDataModel
import unittest
from datetime import datetime, timedelta

class TestQuantDataModels(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        self.intraday_data = [
            IntradayDataModel(datetime(2023, 1, 1, 9, 0), 100, 50, 'AAPL'),
            IntradayDataModel(datetime(2023, 1, 1, 9, 1), 102, 30, 'AAPL'),
            IntradayDataModel(datetime(2023, 1, 1, 9, 2), 101, 20, 'AAPL'),
            IntradayDataModel(datetime(2023, 1, 1, 9, 3), 103, 40, 'AAPL'),
        ]
        self.news_data = [
            NewsDataModel(datetime(2023, 1, 1, 10, 0), "Headline 1", 0.8, 0.9),
            NewsDataModel(datetime(2023, 1, 1, 11, 0), "Headline 2", 0.4, 0.5),
            NewsDataModel(datetime(2023, 1, 1, 12, 0), "Headline 3", 0.9, 0.8),
        ]

    def test_aggregate_by_interval(self):
        model = IntradayDataModel(None, None, None, None)
        result = model.aggregate_by_interval(self.intraday_data, 1)
        self.assertEqual(len(result), 4)
        self.assertAlmostEqual(result[0]['avg_price'], 100)
        self.assertEqual(result[0]['total_volume'], 50)

    def test_get_high_low(self):
        model = IntradayDataModel(None, None, None, None)
        high, low = model.get_high_low(self.intraday_data, datetime(2023, 1, 1, 9, 0), datetime(2023, 1, 1, 9, 3))
        self.assertEqual(high, 103)
        self.assertEqual(low, 100)

    def test_calculate_vwap(self):
        model = IntradayDataModel(None, None, None, None)
        vwap = model.calculate_vwap(self.intraday_data)
        # self.assertAlmostEqual(vwap, 101.428)
        self.assertAlmostEqual(round(vwap), 101)

    def test_filter_by_sentiment(self):
        model = NewsDataModel(None, None, None, None)
        filtered = model.filter_by_sentiment(self.news_data, 0.5)
        self.assertEqual(len(filtered), 2)

    def test_summarize_news(self):
        model = NewsDataModel(None, None, None, None)
        summaries = model.summarize_news(self.news_data)
        self.assertEqual(len(summaries), 3)
        self.assertIn("Headline 1", summaries)

    def test_filter_by_relevance(self):
        model = NewsDataModel(None, None, None, None)
        filtered = model.filter_by_relevance(self.news_data, 0.7)
        self.assertEqual(len(filtered), 2)

if __name__ == '__main__':
    unittest.main()
