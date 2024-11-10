import unittest
from src.models.utils import test_sum
from src.features.data_catalog import DataSet, DataCategory, DataCatalog
from src.exceptions.except_data_catalog import NoNameDataSetError, CategoryMismatchError, NoKeywordsFoundError, DataNotFoundError

class TestDataSet(unittest.TestCase):
    def test_dataset_initialization(self):
        dataset = DataSet(dataset_name="TestDataset", category="Category1", data={"sample": "data"})
        self.assertEqual(dataset.name, "TestDataset")
        self.assertEqual(dataset.category, "Category1")
        self.assertEqual(dataset.data, {"sample": "data"})

    def test_dataset_missing_data(self):
        with self.assertRaises(DataNotFoundError):
            DataSet(dataset_name="TestDataset", category="Category1")

class TestDataCategory(unittest.TestCase):
    def setUp(self):
        self.data_category = DataCategory(name="Category1")

    def test_add_dataset(self):
        dataset = DataSet(dataset_name="TestDataset", category="Category1", data={"sample": "data"})
        self.data_category.add_dataset(dataset)
        self.assertIn("TestDataset", self.data_category.datasets)

    def test_add_dataset_as_dict(self):
        dataset = {"name": "TestDataset", "category": "Category1", "data": {"sample": "data"}}
        self.data_category.add_dataset(dataset)
        self.assertIn("TestDataset", self.data_category.datasets)

    def test_add_dataset_mismatched_category(self):
        dataset = DataSet(dataset_name="TestDataset", category="Category2", data={"sample": "data"})
        with self.assertRaises(CategoryMismatchError) as context:
            self.data_category.add_dataset(dataset)
        self.assertIn("Mismatched Category", str(context.exception))


    def test_search(self):
        dataset = DataSet(dataset_name="TestDataset", category="Category1", data={"sample": "data"})
        self.data_category.add_dataset(dataset)
        matches = self.data_category.search("Test")
        self.assertIn("TestDataset", matches)

        matches = self.data_category.search("NonExistent")
        self.assertEqual(matches, {})

        with self.assertRaises(NoKeywordsFoundError):
            self.data_category.search(None)

class TestDataCatalog(unittest.TestCase):
    def setUp(self):
        self.data_catalog = DataCatalog()
        self.data_catalog.add_category("Category1")

    def test_add_category(self):
        self.data_catalog.add_category("Category2")
        self.assertIn("Category2", self.data_catalog.categories)

    def test_add_dataset(self):
        dataset = DataSet(dataset_name="TestDataset", category="Category1", data={"sample": "data"})
        # print(f"self.datasets: {self.data_catalog.categories['Category1'].datasets}")
        self.data_catalog.add_dataset("Category1", dataset)
        # print(f"self.datasets: {self.data_catalog.categories['Category1'].datasets}")
        self.assertIn(dataset, self.data_catalog.categories["Category1"].datasets.values())

    def test_add_dataset_as_dict(self):
        dataset = {"name": "TestDataset", "category": "Category1", "data": {"sample": "data"}}
        self.data_catalog.add_dataset("Category1", dataset)
        
        # Check if the dataset name is in the datasets dictionary
        self.assertIn("TestDataset", self.data_catalog.categories["Category1"].datasets.keys())
        
        print(self.data_catalog.categories["Category1"].datasets)
        added_dataset = self.data_catalog.categories["Category1"].datasets["TestDataset"]
        self.assertEqual(added_dataset.name, "TestDataset")
        self.assertEqual(added_dataset.category, "Category1")
        self.assertEqual(added_dataset.data, {"sample": "data"})


    def test_list_datasets(self):
        dataset = DataSet(dataset_name="TestDataset", category="Category1", data={"sample": "data"})
        self.data_catalog.add_dataset("Category1", dataset)
        datasets = self.data_catalog.list_datasets("Category1")
        self.assertIn("TestDataset", datasets)

    def test_search_data(self):
        dataset = DataSet(dataset_name="TestDataset", category="Category1", data={"sample": "data"})
        self.data_catalog.add_dataset("Category1", dataset)
        results = self.data_catalog.search_data("Test")
        self.assertIn("TestDataset", results)

if __name__ == '__main__':
    unittest.main()
