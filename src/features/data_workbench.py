from src.models.utils import test_sum
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import timedelta
from src.exceptions.except_data_catalog import DataNotFoundError

def test_double(a):
    return test_sum(a,a)
 
'''
3. Data Workbench

The Data Workbench is the platform’s workspace where data is transformed, processed, and stored in a structured form for analysis. This component allows researchers to access, modify, and update data, ensuring it is clean and analysis-ready.

what transformations lol, vague asf, can a transformation be visualising data?

'''

class DataWorkbench:

    def __init__(self):

        self.data_storage = {}


    def store_data(self, dataset_name, data):

        self.data_storage[dataset_name] = data


    def retrieve_data(self, dataset_name):

        return self.data_storage.get(dataset_name, DataNotFoundError())
 

    def transform_data(self, dataset_name, transformation_func):

        data = self.retrieve_data(dataset_name)

        return transformation_func(data) if data else DataNotFoundError()
    
    def filter_data(self, data, condition):
        return [entry for entry in data if condition(entry)]

    def aggregate_data(self, data, interval):
        # Example aggregation by interval for intraday data
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

    def plot_sentiment_over_time(self, data):
        # Plot sentiment scores over time.
        timestamps = [entry.timestamp for entry in data]
        sentiment_scores = [entry.sentiment_score for entry in data]

        plt.figure(figsize=(10, 5))
        plt.plot(timestamps, sentiment_scores, marker='o', linestyle='-', color='b')
        plt.xlabel('Time')
        plt.ylabel('Sentiment Score')
        plt.title('Sentiment Score over Time')
        plt.grid(True)
        plt.show()

    def plot_relevance_distribution(self, data):
        # Plot the distribution of relevance scores.
        relevance_scores = [entry.relevance for entry in data]

        plt.figure(figsize=(10, 5))
        plt.hist(relevance_scores, bins=10, color='g', alpha=0.7)
        plt.xlabel('Relevance Score')
        plt.ylabel('Frequency')
        plt.title('Relevance Score Distribution')
        plt.grid(True)
        plt.show()

    def plot_price_volume(self, data):
        # Plot price and volume over time.
        timestamps = [entry.timestamp for entry in data]
        prices = [entry.price for entry in data]
        volumes = [entry.volume for entry in data]

        fig, ax1 = plt.subplots()

        color = 'tab:blue'
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Price', color=color)
        ax1.plot(timestamps, prices, color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()  
        color = 'tab:green'
        ax2.set_ylabel('Volume', color=color)  
        ax2.plot(timestamps, volumes, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()  
        plt.title('Price and Volume over Time')
        plt.show()

dataworkbench = DataWorkbench()


    
