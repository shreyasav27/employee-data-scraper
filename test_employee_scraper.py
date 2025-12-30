import pandas as pd
import requests
from unittest.mock import patch, Mock

from employee_scrapper import fetch_employee_data


# Test Case 1: Verify JSON File Download
def test_api_download():
    data = fetch_employee_data()
    assert data is not None
    assert isinstance(data, list)


# Test Case 2: Verify JSON File Extraction
def test_json_extraction():
    data = fetch_employee_data()
    assert "first_name" in data[0]
    assert "last_name" in data[0]
    assert "email" in data[0]


# Test Case 3 Validate File Type and Format
def test_file_type_and_format():
    data = fetch_employee_data()
    df = pd.DataFrame(data)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty


# Test Case 4: Validate Data Structure
def test_data_structure():
    data = fetch_employee_data()
    df = pd.DataFrame(data)

    expected_columns = {
        "first_name",
        "last_name",
        "email",
        "phone",
        "gender",
        "age",
        "job_title",
        "years_of_experience",
        "salary",
        "department"
    }

    assert expected_columns.issubset(df.columns)


# Test Case 5: Handle Missing or Invalid Data
@patch("requests.get")
def test_handle_missing_or_invalid_data(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone": "123x456",
            "gender": "Male",
            "age": "30",
            "job_title": "Engineer",
            "years_of_experience": "5",
            "salary": "70000",
            "department": "IT"
        }
    ]

    mock_get.return_value = mock_response

    data = fetch_employee_data()
    df = pd.DataFrame(data)

    assert df.loc[0, "phone"] == "123x456"
