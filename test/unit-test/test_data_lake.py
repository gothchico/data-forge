import unittest
from src.features.data_lake import DataLake

class TestDataLake(unittest.TestCase):
    def setUp(self):
        # Set up a DataLake object for testing
        self.data_lake = DataLake()

    def test_store_and_retrieve_raw_data(self):
        # Test storing and retrieving raw data
        self.data_lake.store_data("Dataset1", [1, 2, 3], processed=False)
        data = self.data_lake.retrieve_data("Dataset1", processed=False)
        self.assertEqual(data, [1, 2, 3])

    def test_store_and_retrieve_processed_data(self):
        # Test storing and retrieving processed data
        self.data_lake.store_data("Dataset2", [4, 5, 6], processed=True)
        data = self.data_lake.retrieve_data("Dataset2", processed=True)
        self.assertEqual(data, [4, 5, 6])

    def test_retrieve_nonexistent_data(self):
        # Test retrieving data that does not exist
        data = self.data_lake.retrieve_data("NonExistentDataset", processed=False)
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()
