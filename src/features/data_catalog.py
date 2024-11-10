from src.models.utils import test_sum
from src.exceptions.except_data_catalog import DataNotFoundError, CategoryMismatchError, NoKeywordsFoundError, NoNameDataSetError
import re

def test_double(a):
    return test_sum(a, a)

class DataSet:
    def __init__(self, dataset_name=None, category=None, data=None, **kwargs):
        if data is None:
            raise DataNotFoundError()

        self.name = dataset_name or kwargs.get("name", "Unnamed")
        self.category = category or kwargs.get("category", "Uncategorized")
        self.data = data
        self.metadata = kwargs or kwargs.get("metadata", None)

        if isinstance(self.data, dict):
            self.name = self.name or self.data.get("name", "Unnamed")
            self.category = self.category or self.data.get("category", "Uncategorized")

        if not self.name or not self.category:
            raise DataNotFoundError()


class DataCategory:
    def __init__(self, name=None):
        self.datasets = {}
        self.name = name

    def add_dataset(self, dataset):
        # Check if dataset is a dictionary, and extract fields if so
        if isinstance(dataset, dict):
            dataset_name = dataset.get("name")
            if dataset_name is None:
                raise NoNameDataSetError()
            
            dataset_category = dataset.get("category", self.name)
            data = dataset.get("data")
            clean_dataset = {k: v for k, v in dataset.items() if k not in ["name", "category", "data"]}
            dataset = DataSet(dataset_name=dataset_name, category=dataset_category, data=data, **clean_dataset)
        else:
            dataset_name = dataset.name  #get the name directly
        
        if dataset.category == self.name:
            self.datasets[dataset_name] = dataset
        else:
            raise CategoryMismatchError(name=self.name, category=dataset.category)


    def search(self, keywords=None):
        if keywords is None:
            raise NoKeywordsFoundError()
        
        matches_found = {}
        for name, dataset in self.datasets.items():
            print(f"Searching in category: {name}")
            if isinstance(keywords, list):
                for kw in keywords:
                    kw_str = str(kw)
                    print(f"Keyword: {kw_str}")
                    if re.search(re.escape(kw_str), name):
                        matches_found[name] = dataset
            else:
                keyword_str = str(keywords)
                print(f"Single keyword search: {keyword_str}")
                if re.search(re.escape(keyword_str), name):
                    matches_found[name] = dataset

        if matches_found:
                print("\n------------------ data lake retrieval --------------------------\nmatches found for keywords {keywords}: {list(matches_found.keys())}")
        else:
            print("No matches found in dataset names, performing dataset level search...")
            for d in self.datasets.values():
                print(f"\nsearching in category: {name}")
                keyword_str = str(keywords)
                print(f"single keyword search: {keyword_str}")
                if re.search(re.escape(keyword_str), d.name):
                    print(f"\ndataset-level match found! dataset: {d.name} in category: {d.category}")
                    matches_found[d.name] = dataset
        
        return matches_found

class DataCatalog:
    def __init__(self):
        self.categories = {}

    def add_category(self, name):
        if name not in self.categories:
            self.categories[name] = DataCategory(name)

    def add_dataset(self, category_name, dataset):
        # Ensure the category exists, then add the dataset to it
        if category_name not in self.categories:
            self.add_category(category_name)
        self.categories[category_name].add_dataset(dataset)

    def list_datasets(self, category_name):
        if category_name in self.categories:
            return [dataset.name for dataset in self.categories[category_name].datasets.values()]
        raise CategoryMismatchError(category_name=category_name)

    def search_data(self, keywords):
        results = []
        for category in self.categories.values():
            results.extend(category.search(keywords).keys())
        return results
