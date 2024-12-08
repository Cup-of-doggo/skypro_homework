import os
from src.utils import get_json_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path_file_operations = os.path.join(BASE_DIR, "..", "data", "operations.json")


def test_get_json_data():
    get_json_data()
    assert path_file_operations
