from src.models.utils import test_sum

def test_double(a):
    return test_sum(a,a)
 
class DataLake:

    def __init__(self):

        self.raw_data = {}

        self.processed_data = {}

    def store_data(self, dataset_name, data, processed=False):
        if processed:

            self.processed_data[dataset_name] = data
            # print(f"Stored in processed data: {self.processed_data}")

        else:

            self.raw_data[dataset_name] = data
            # print(f"Stored in raw data: {self.raw_data}")

    def retrieve_data(self, dataset_name, processed=False):
        
        return self.processed_data.get(dataset_name) if processed else self.raw_data.get(dataset_name)
