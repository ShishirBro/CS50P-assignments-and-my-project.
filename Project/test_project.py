import pytest
from unittest.mock import patch, Mock
from project import fetch_data


def test_fetch_data():
    # Mock the requests.get call to return a fake response
    with patch('requests.get') as mock_get:
        # Setup the mock to return a specific response when called
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = {
            'properties': {
                'parameter': {
                    'PRECTOTCORR': {
                        '20200101': 0.5,
                        '20200102': 0.7
                    }
                }
            }
        }
        mock_get.return_value = mock_response

        # Test with dummy parameters
        response = fetch_data(55, -87, '20200101', '20200102')

        # Check that the function returns the correct data
        assert response == mock_response.json.return_value
        mock_response.raise_for_status.assert_called_once()  # Ensure it checks for HTTP errors