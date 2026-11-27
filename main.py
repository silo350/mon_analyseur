import logging

from src.extract import get_regions

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    regions = get_regions()
    print(regions)