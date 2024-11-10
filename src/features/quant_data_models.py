# 4. Quant Data Models
# 
# Quant Data Models define the structure for various data types, such as Intraday Data and News Data. 
# These models standardize how data is accessed, ensuring consistent and efficient data handling.
# 
# Example Code (for guidance only):

from datetime import datetime, timedelta
from collections import defaultdict

class IntradayDataModel:
    def __init__(self, timestamp, price, volume, symbol):
        self.timestamp = timestamp
        self.price = price
        self.volume = volume
        self.symbol = symbol

    def aggregate_by_interval(self, data, interval):
        # Group data points into specified intervals (e.g., minute, hour) 
        # and calculate average price or total volume for each interval.
        aggregated_data = defaultdict(lambda: {'price_sum': 0, 'volume_sum': 0, 'count': 0})
        for entry in data:
            bucket = entry.timestamp - timedelta(minutes=entry.timestamp.minute % interval,
                                                 seconds=entry.timestamp.second,
                                                 microseconds=entry.timestamp.microsecond)
            aggregated_data[bucket]['price_sum'] += entry.price * entry.volume
            aggregated_data[bucket]['volume_sum'] += entry.volume
            aggregated_data[bucket]['count'] += 1
        
        result = []
        for bucket, values in aggregated_data.items():
            avg_price = values['price_sum'] / values['volume_sum'] if values['volume_sum'] != 0 else 0
            result.append({'timestamp': bucket, 'avg_price': avg_price, 'total_volume': values['volume_sum']})
        
        return result

    def get_high_low(self, data, start_time, end_time):
        # Get the highest and lowest prices between a given time range.
        filtered_data = [entry for entry in data if start_time <= entry.timestamp <= end_time]
        if not filtered_data:
            return None, None

        high_price = max(entry.price for entry in filtered_data)
        low_price = min(entry.price for entry in filtered_data)
        return high_price, low_price

    def calculate_vwap(self, data):
        # VWAP (Volume Weighted Average Price) calculation.
        total_price_volume = sum(entry.price * entry.volume for entry in data)
        total_volume = sum(entry.volume for entry in data)
        vwap = total_price_volume / total_volume if total_volume != 0 else 0
        return vwap

class NewsDataModel:
    def __init__(self, timestamp, headline, sentiment_score, relevance):
        self.timestamp = timestamp
        self.headline = headline
        self.sentiment_score = sentiment_score
        self.relevance = relevance

    def filter_by_sentiment(self, data, threshold):
        # Filter news items by checking if the sentiment score exceeds a threshold.
        filtered_news = [entry for entry in data if entry.sentiment_score >= threshold]
        return filtered_news

    def summarize_news(self, data):
        # Simple summarization of news articles based on the headlines.
        summaries = [entry.headline for entry in data]
        return summaries

    def filter_by_relevance(self, data, relevance_threshold):
        # Filter news articles to include only those with relevance above the threshold.
        filtered_news = [entry for entry in data if entry.relevance >= relevance_threshold]
        return filtered_news
