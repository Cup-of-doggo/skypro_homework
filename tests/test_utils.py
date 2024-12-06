import os
from src.utils import get_date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path_file_operations = os.path.join(BASE_DIR, "..", "data", "operations.json")


def test_get_date():
    get_date()
    assert path_file_operations
