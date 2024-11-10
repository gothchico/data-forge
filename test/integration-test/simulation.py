from datetime import datetime
from src.features.quant_data_models import IntradayDataModel, NewsDataModel
from src.features.data_workbench import DataWorkbench
from src.features.data_catalog import DataCatalog
from src.features.data_lake import DataLake

def main():
    print("\n------------------ starting simulation --------------------------")
    
    # initialize components
    print("\ninitializing data workbench, data lake, and data catalog...")
    workbench = DataWorkbench()
    data_lake = DataLake()
    data_catalog = DataCatalog()
    
    # generating test data for intraday data model
    print("\ngenerating test data for the intraday data model...")
    intraday_data = [
        IntradayDataModel(datetime(2023, 1, 1, 9, 0), 100, 50, 'AAPL'),
        IntradayDataModel(datetime(2023, 1, 1, 9, 1), 102, 30, 'AAPL'),
        IntradayDataModel(datetime(2023, 1, 1, 9, 2), 101, 20, 'AAPL'),
        IntradayDataModel(datetime(2023, 1, 1, 9, 3), 103, 40, 'AAPL'),
        IntradayDataModel(datetime(2023, 1, 1, 9, 4), 104, 25, 'AAPL')
    ]
    data_lake.store_data('intraday_data', intraday_data)
    print("intraday data stored in data lake.")
    print("\n------------------ simulating data catalog --------------------------")
    # adding dataset to catalog with metadata
    print("\nadding intraday dataset to the data catalog with metadata...")
    data_catalog.add_dataset('intraday_data', {
        'name': 'AAPL',
        'category': 'intraday_data',
        'data': intraday_data,
        'metadata': ['AAPL', 'stock', 'intraday', 'finance']
    })
    print("dataset 'AAPL' added to catalog under 'intraday_data' category.")
    print("\n------------------ workbench aggregation --------------------------")
    # retrieving and transforming data

    print("\nretrieving raw intraday data from data lake for aggregation...")
    raw_data = data_lake.retrieve_data('intraday_data')
    aggregated_data = workbench.aggregate_data(raw_data, 1)
    print("\naggregated data (by minute interval):")
    for entry in aggregated_data:
        print(f"timestamp: {entry['timestamp']}, avg price: {entry['avg_price']}, total volume: {entry['total_volume']}")

    # generating test data for news data model
    print("\ngenerating test data for news data model...")
    news_data = [
        NewsDataModel(datetime(2023, 1, 1, 10, 0), "market opens with gains", 0.8, 0.9),
        NewsDataModel(datetime(2023, 1, 1, 11, 0), "tech stocks rally", 0.4, 0.7),
        NewsDataModel(datetime(2023, 1, 1, 12, 0), "AAPL reaches all-time high", 0.9, 0.95),
        NewsDataModel(datetime(2023, 1, 1, 13, 0), "economic forecast remains steady", 0.5, 0.4)
    ]
    data_lake.store_data('news_data', news_data)
    print("news data stored in data lake.")

    # searching dataset in catalog
    print("\n------------------ data catalog search --------------------------")
    print("\nsearching 'AAPL' in data catalog...")
    search_result = data_catalog.search_data('AAPL')
    print("search result:", search_result)
    
    print("\n------------------ workbench filtering --------------------------")

    # filtering news data by sentiment
    print("\nfiltering news data by sentiment score threshold (0.5)...")
    filtered_news = NewsDataModel(None, None, None, None).filter_by_sentiment(news_data, 0.5)
    print("filtered news based on sentiment (>= 0.5):")
    for news in filtered_news:
        print(f"headline: {news.headline}, sentiment score: {news.sentiment_score}")

    # filtering news data by relevance
    print("\nfiltering news data by relevance threshold (0.8)...")
    filtered_relevance_news = NewsDataModel(None, None, None, None).filter_by_relevance(news_data, 0.8)
    print("filtered news based on relevance (>= 0.8):")
    for news in filtered_relevance_news:
        print(f"headline: {news.headline}, relevance: {news.relevance}")

    # calculating VWAP for intraday data
    print("\ncalculating VWAP for AAPL intraday data...")
    vwap = IntradayDataModel(None, None, None, None).calculate_vwap(intraday_data)
    print(f"VWAP for AAPL: {vwap}")

    # getting high and low prices within a specific range
    print("\ngetting high and low prices for AAPL from 9:00 to 9:03...")
    high, low = IntradayDataModel(None, None, None, None).get_high_low(
        intraday_data, datetime(2023, 1, 1, 9, 0), datetime(2023, 1, 1, 9, 3)
    )
    print(f"high price: {high}, low price: {low}")

    print("\n------------------ simulation complete --------------------------\n")

if __name__ == "__main__":
    main()
