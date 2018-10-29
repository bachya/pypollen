"""Define fixtures for "Asthma"."""
import pytest


@pytest.fixture()
def fixture_extended():
    """Return a /forecast/extended/asthma/<ZIP> response."""
    return {
        "Type": "asthma",
        "ForecastDate": "2018-10-28T00:00:00-04:00",
        "Location": {
            "ZIP": "73344",
            "City": "AUSTIN",
            "State": "TX",
            "periods": [{
                "Period": "2018-10-28T05:45:01.45",
                "Index": 4.5,
                "Idx": "4.5"
            }, {
                "Period": "2018-10-29T05:45:01.45",
                "Index": 4.7,
                "Idx": "4.7"
            }, {
                "Period": "2018-10-30T05:45:01.45",
                "Index": 5.0,
                "Idx": "5.0"
            }, {
                "Period": "2018-10-31T05:45:01.45",
                "Index": 5.2,
                "Idx": "5.2"
            }, {
                "Period": "2018-11-01T05:45:01.45",
                "Index": 5.5,
                "Idx": "5.5"
            }],
            "DisplayLocation":
                "Austin, TX"
        }
    }
