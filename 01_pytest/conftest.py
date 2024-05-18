import pytest

from storage import storage


@pytest.fixture
def website_data():
    return storage.website_data
