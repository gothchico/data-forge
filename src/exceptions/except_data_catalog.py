class DataNotFoundError(BaseException):
    def __init__(self):
        print("data not found")

class CategoryMismatchError(Exception):
    def __init__(self, name=None, category=None):
        if name and category:
            # For mismatched categories
            self.message = f"Mismatched Category: current category is '{name}' and dataset category is '{category}'."
        elif name:
            # For category not found
            self.message = f"Category '{name}' not found."
        else:
            self.message = "Category mismatch error."
        
        super().__init__(self.message)

class NoKeywordsFoundError(BaseException):
    def __init__(self):
        print(f'No keywords passed!!!')

class NoNameDataSetError(BaseException):
    def __init__(self):
        print(f'Dataset doesn\'t have a name!')