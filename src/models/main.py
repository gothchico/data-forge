from src.models import test_double, test_sum
from src.models.config import config

def main():
    print(test_double(config.NUM_EPOCHS))

if __name__ == "__main__":
    main()