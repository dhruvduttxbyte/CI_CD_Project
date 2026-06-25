import pytest
from scraper import fetch_quotes

def test_http_request_and_parsing():
    """Test that ensures requests gets data and selectors extract it properly"""
    data = fetch_quotes()
    # Verify we got a list back
    assert isinstance(data, list)
    # Verify the request fetched exactly 10 quotes from the first page
    assert len(data) == 10
    # Structural check on the dictionary keys
    assert "quote" in data[0]
    assert "author" in data[0]