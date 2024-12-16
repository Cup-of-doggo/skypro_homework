from unittest.mock import patch
from src.file_readers import get_csv_file, get_excel_file


@patch('csv.DictReader')
def test_get_csv_file(mock_read):
    mock_read.return_value.csv.return_value = []
    assert get_csv_file() == []


@patch('pandas.read_excel')
def test_get_excel_file(mock_read):
    mock_read.return_value = []
    assert get_excel_file() == []