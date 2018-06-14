"""Define tests for the "Supported" object."""
# pylint: disable=redefined-outer-name,unused-import

import json

import aiohttp
import pytest

from pypollencom import Client
from pypollencom.errors import InvalidZipError

from .const import TEST_BAD_ZIP, TEST_ZIP


@pytest.fixture(scope='module')
def fixture_current():
    """Return a /forecast/current/pollen/<ZIP> response."""
    return {
        "Type": "pollen",
        "ForecastDate": "2018-06-12T00:00:00-04:00",
        "Location": {
            "ZIP":
                "80238",
            "City":
                "DENVER",
            "State":
                "CO",
            "periods": [{
                "Triggers": [{
                    "LGID": 272,
                    "Name": "Juniper",
                    "Genus": "Juniperus",
                    "PlantType": "Tree"
                }, {
                    "LGID": 346,
                    "Name": "Grasses",
                    "Genus": "Grasses",
                    "PlantType": "Grass"
                }, {
                    "LGID": 63,
                    "Name": "Chenopods",
                    "Genus": "Chenopods",
                    "PlantType": "Ragweed"
                }],
                "Period":
                    "0001-01-01T00:00:00",
                "Type":
                    "Yesterday",
                "Index":
                    7.2
            }, {
                "Triggers": [{
                    "LGID": 272,
                    "Name": "Juniper",
                    "Genus": "Juniperus",
                    "PlantType": "Tree"
                }, {
                    "LGID": 346,
                    "Name": "Grasses",
                    "Genus": "Grasses",
                    "PlantType": "Grass"
                }, {
                    "LGID": 63,
                    "Name": "Chenopods",
                    "Genus": "Chenopods",
                    "PlantType": "Ragweed"
                }],
                "Period":
                    "0001-01-01T00:00:00",
                "Type":
                    "Today",
                "Index":
                    6.6
            }, {
                "Triggers": [{
                    "LGID": 272,
                    "Name": "Juniper",
                    "Genus": "Juniperus",
                    "PlantType": "Tree"
                }, {
                    "LGID": 346,
                    "Name": "Grasses",
                    "Genus": "Grasses",
                    "PlantType": "Grass"
                }, {
                    "LGID": 63,
                    "Name": "Chenopods",
                    "Genus": "Chenopods",
                    "PlantType": "Ragweed"
                }],
                "Period":
                    "0001-01-01T00:00:00",
                "Type":
                    "Tomorrow",
                "Index":
                    6.3
            }],
            "DisplayLocation":
                "Denver, CO"
        }
    }


@pytest.fixture(scope='module')
def fixture_empty_response():
    """Return a 200 response that has no data."""
    return {
        "Type": "pollen",
        "ForecastDate": "2018-06-14T00:00:00-04:00",
        "Location": {
            "ZIP": "a",
            "periods": []
        }
    }


@pytest.fixture(scope='module')
def fixture_extended():
    """Return a /forecast/extended/pollen/<ZIP> response."""
    return {
        "Type": "pollen",
        "ForecastDate": "2018-06-12T00:00:00-04:00",
        "Location": {
            "ZIP":
                "80238",
            "City":
                "DENVER",
            "State":
                "CO",
            "periods": [{
                "Period": "2018-06-12T13:47:12.897",
                "Index": 6.60
            }, {
                "Period": "2018-06-13T13:47:12.897",
                "Index": 6.30
            }, {
                "Period": "2018-06-14T13:47:12.897",
                "Index": 7.60
            }, {
                "Period": "2018-06-15T13:47:12.897",
                "Index": 7.60
            }, {
                "Period": "2018-06-16T13:47:12.897",
                "Index": 7.30
            }],
            "DisplayLocation":
                "Denver, CO"
        }
    }


@pytest.fixture(scope='module')
def fixture_historic():
    """Return a /forecast/historic/pollen/<ZIP> response."""
    return {
        "Type": "pollen",
        "ForecastDate": "2018-06-12T00:00:00-04:00",
        "Location": {
            "ZIP":
                "80238",
            "City":
                "DENVER",
            "State":
                "CO",
            "periods": [{
                "Period": "2018-05-14T05:30:05",
                "Index": 4.30
            }, {
                "Period": "2018-05-15T05:30:06",
                "Index": 6.90
            }, {
                "Period": "2018-05-16T07:25:27",
                "Index": 8.90
            }, {
                "Period": "2018-05-17T05:30:06",
                "Index": 9.30
            }, {
                "Period": "2018-05-18T05:30:10",
                "Index": 7.60
            }, {
                "Period": "2018-05-19T05:30:21",
                "Index": 0.90
            }, {
                "Period": "2018-05-20T05:30:36",
                "Index": 6.70
            }, {
                "Period": "2018-05-21T05:30:03",
                "Index": 8.50
            }, {
                "Period": "2018-05-22T05:30:07",
                "Index": 8.90
            }, {
                "Period": "2018-05-23T05:30:02",
                "Index": 8.90
            }, {
                "Period": "2018-05-24T05:30:10",
                "Index": 8.50
            }, {
                "Period": "2018-05-25T05:30:07",
                "Index": 8.60
            }, {
                "Period": "2018-05-26T05:30:06",
                "Index": 9.00
            }, {
                "Period": "2018-05-27T05:30:09",
                "Index": 9.10
            }, {
                "Period": "2018-05-28T05:30:11",
                "Index": 7.40
            }, {
                "Period": "2018-05-29T05:30:06",
                "Index": 7.70
            }, {
                "Period": "2018-05-30T05:30:07",
                "Index": 8.00
            }, {
                "Period": "2018-05-31T05:30:05",
                "Index": 8.10
            }, {
                "Period": "2018-06-01T05:30:04",
                "Index": 8.40
            }, {
                "Period": "2018-06-02T05:30:08",
                "Index": 8.00
            }, {
                "Period": "2018-06-03T05:30:37",
                "Index": 7.80
            }, {
                "Period": "2018-06-04T05:30:03",
                "Index": 7.90
            }, {
                "Period": "2018-06-05T05:30:08",
                "Index": 8.00
            }, {
                "Period": "2018-06-06T05:30:08",
                "Index": 7.50
            }, {
                "Period": "2018-06-07T05:30:05",
                "Index": 7.70
            }, {
                "Period": "2018-06-08T05:30:06",
                "Index": 7.90
            }, {
                "Period": "2018-06-09T05:30:15",
                "Index": 7.70
            }, {
                "Period": "2018-06-10T05:30:09",
                "Index": 8.00
            }, {
                "Period": "2018-06-11T05:30:00",
                "Index": 7.20
            }, {
                "Period": "2018-06-12T05:30:04",
                "Index": 6.60
            }],
            "DisplayLocation":
                "Denver, CO"
        }
    }


@pytest.fixture(scope='module')
def fixture_outlook():
    """Return a /forecast/outlook/<ZIP> response."""
    return {
        "Market": "DENVER, CO",
        "ZIP": "80238",
        "TrendID": 4,
        "Trend": "subsiding",
        "Outlook": "The amount of pollen in the air for Wednesday...",
        "Season": "Tree"
    }


@pytest.mark.asyncio
async def test_endpoints(  # pylint: disable=too-many-arguments
        aresponses, event_loop, fixture_current, fixture_extended,
        fixture_historic, fixture_outlook):
    """Test all endpoints."""
    aresponses.add(
        'www.pollen.com',
        '/api/forecast/current/pollen/{0}'.format(TEST_ZIP), 'get',
        aresponses.Response(text=json.dumps(fixture_current), status=200))
    aresponses.add(
        'www.pollen.com', '/api/forecast/extended/pollen/{0}'.format(TEST_ZIP),
        'get',
        aresponses.Response(text=json.dumps(fixture_extended), status=200))
    aresponses.add(
        'www.pollen.com', '/api/forecast/historic/pollen/{0}'.format(TEST_ZIP),
        'get',
        aresponses.Response(text=json.dumps(fixture_historic), status=200))
    aresponses.add(
        'www.pollen.com', '/api/forecast/outlook/{0}'.format(TEST_ZIP), 'get',
        aresponses.Response(text=json.dumps(fixture_outlook), status=200))

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        current = await client.allergens.current()
        assert len(current['Location']['periods']) == 3

        extended = await client.allergens.extended()
        assert len(extended['Location']['periods']) == 5

        historic = await client.allergens.historic()
        assert len(historic['Location']['periods']) == 30

        outlook = await client.allergens.outlook()
        assert outlook['Trend'] == 'subsiding'


@pytest.mark.asyncio
async def test_bad_zip(aresponses, event_loop, fixture_empty_response):
    """Test the cases that would arise from a bad ZIP code."""
    aresponses.add(
        'www.pollen.com',
        '/api/forecast/current/pollen/{0}'.format(TEST_BAD_ZIP), 'get',
        aresponses.Response(
            text=json.dumps(fixture_empty_response), status=200))
    aresponses.add(
        'www.pollen.com', '/api/forecast/outlook/{0}'.format(TEST_BAD_ZIP),
        'get', aresponses.Response(text='', status=404))

    with pytest.raises(InvalidZipError):
        async with aiohttp.ClientSession(loop=event_loop) as websession:
            client = Client(TEST_BAD_ZIP, websession)
            await client.allergens.current()

    with pytest.raises(InvalidZipError):
        async with aiohttp.ClientSession(loop=event_loop) as websession:
            client = Client(TEST_BAD_ZIP, websession)
            await client.allergens.outlook()
